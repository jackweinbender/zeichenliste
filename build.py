# This file is for pulling the data down from 
# Google Docs and generating the data files that 
# we use to power this thing.

import os, requests, json

# Spreadsheet details
SPREADSHEET_ID = '1H3OsWtoybznhHtFzSxamPzEvCoQGOhM8sJXYOrNtsgw'
URL = f'https://spreadsheets.google.com/feeds/list/{SPREADSHEET_ID}/od6/public/values?alt=json'

data = requests.get(URL).json()
rows = data['feed']['entry']

signlist = {}

for row in rows:

    borger = row['gsx$borger']['$t']

    signlist[borger] = {
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


with open('data/signlist.json', 'w') as outfile:
    json.dump(signlist, outfile, ensure_ascii=False, sort_keys=True, indent=4)