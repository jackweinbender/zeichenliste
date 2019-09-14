# This file is for pulling the data down from 
# Google Docs and generating the data files that 
# we use to power this thing.

import requests, json, os
from collections import defaultdict
from models.sign import Sign
from models.sign_value import SignValue
from models.normalizer import Normalizer

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

# Dump the latest sheet into the test data so we know we don't break anything
path = os.path.dirname(os.path.dirname(os.path.dirname( __file__ ))) + '/test/data/sheets-cache.json'
with open(path, 'w') as outfile:
    json.dump(rows, outfile, ensure_ascii=False, sort_keys=True, indent=4)

# The output SIGNLIST
signlist = {}
index = defaultdict(list)

for row in rows:
    # Gets the Borger number for the KEY
    borger = row['gsx$borger']['$t']

    # Serialize the row as a Sign Object
    sign = Sign.from_sheets_row(row)
    
    # Add Sign to signlist (as dict, for later JSON output)
    signlist[borger] = sign.__dict__

    # Add Borger_id to all index values
    indexed_keys = [
        'borger_id', 
        'labat_id', 
        'huehnergard_id', 
        'deimel_id', 
        'mittermayer_id', 
        'hethzl_id',
        # 'labat_name',
        # 'borger_name', 
        # 'oracc_name',
        # 'unicode_name',
    ]

    # Make the index for signlist numbers
    for k in indexed_keys:
        # Get property value by name
        val = getattr(sign,k)
        idx = val.lower()
        # Add Borger ID to index
        if val != '' and sign.borger_id not in index[idx]:
            index[idx].append(sign.borger_id)

    for value in sign.values:
        vs = SignValue(value).get_keys()
        for v in vs:
            idx = Normalizer.normalize(v)
            if sign.borger_id not in index[idx]:
                index[idx].append(sign.borger_id)

with open(os.path.dirname(os.path.dirname( __file__ )) +'/signlist.json', 'w') as outfile:
    json.dump(signlist, outfile, ensure_ascii=False, sort_keys=True, indent=4)

with open(os.path.dirname(os.path.dirname( __file__ )) + '/search_index.json', 'w') as outfile:
    json.dump(index, outfile, ensure_ascii=False, sort_keys=True, indent=4)