# This file is for pulling the data down from 
# Google Docs and generating the data files that 
# we use to power this thing.

import os, requests, json
from collections import defaultdict
from models.sign import Sign

def cleanup(d):
    d['oracc_name'] = d['oracc_name'][1:]

    for k,v in d.items():
        d[k] = v.strip()

    return d

# Spreadsheet details
SPREADSHEET_ID = '1H3OsWtoybznhHtFzSxamPzEvCoQGOhM8sJXYOrNtsgw'
URL = f'https://spreadsheets.google.com/feeds/list/{SPREADSHEET_ID}/od6/public/values?alt=json'

# Get the data
data = requests.get(URL).json()
# Drill down to the stuff we care about (Rows is a LIST)
rows = data['feed']['entry']

# The output SIGNLIST
signlist = {}
index = defaultdict(list)

for row in rows:
    # Gets the Borger number for the KEY
    borger = row['gsx$borger']['$t']
    
    sign_dict = {
        'oracc_name':     row['gsx$oraccname']['$t'],
        'unicode_name':   row['gsx$unicodename']['$t'],
        'values':         row['gsx$values']['$t'],
        'borger_id':      row['gsx$borger']['$t'],
        'borger_name':    row['gsx$borgername']['$t'],
        'labat_id':       row['gsx$labat']['$t'],
        'labat_name':     row['gsx$labatname']['$t'],
        'huehnergard_id': row['gsx$huehnergard']['$t'],
        'deimel_id':      row['gsx$deimel']['$t'],
        'mittermayer_id': row['gsx$mittermayer']['$t'],
        'hethzl_id':      row['gsx$hethzl']['$t'],
        'unicode_value':  row['gsx$unicode']['$t'],
        # 'hinke_id': row['gsx$hinke']['$t'],
        # 'clay_id': row['gsx$clay']['$t'],
        # 'ranke_id': row['gsx$ranke']['$t']
    }

    sign_dict = cleanup(sign_dict)

    # Serialize the row as a Sign Object
    sign = Sign(sign_dict)
    
    # Add Sign to signlist (as dict, for later JSON output)
    signlist[borger] = sign.__dict__

    # Add Borger_id to all index values
    indexed_keys = [
        # 'oracc_name',
        # 'unicode_name',
        'borger_id', 
        # 'borger_name', 
        'labat_id', 
        # 'labat_name',
        'huehnergard_id', 
        'deimel_id', 
        'mittermayer_id', 
        'hethzl_id'
    ]

    for k in indexed_keys:
        # Get property value by name
        val = getattr(sign,k)
        # Add Borger ID to index
        if val != '' and sign.borger_id not in index[val.lower()]:
            index[val.lower()].append(sign.borger_id)

with open('data/signlist.json', 'w') as outfile:
    json.dump(signlist, outfile, ensure_ascii=False, sort_keys=True, indent=4)

with open('data/search_index.json', 'w') as outfile:
    json.dump(index, outfile, ensure_ascii=False, sort_keys=True, indent=4)