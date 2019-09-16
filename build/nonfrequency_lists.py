# This file generate json files
# with values (no freqs) for OAkk (and eventually MB, MA?)

import os, re, json, unicodedata, operator
from string import printable

# Open file with the 196 syllabic values in OAkk
path = os.path.dirname(os.path.dirname( __file__ )) + '/OAkk_syllabic.txt'
with open(path) as words_file:
    signs = words_file.read().splitlines()

### Associate the values with Borger numbers and generate json
# Create a dict "borger_values" with "value":"borger_number"
borger_values = {}
path = os.path.dirname(os.path.dirname(__file__)) + '/signlist.json'
with open(path) as json_file: data = json.load(json_file)
for record in data.keys():
    for value in data[record]['values']:
        borger_values[value] = record

OAkk_values = {}

# Look for borger_value for every sign
for sign in signs:
    if sign in borger_values.keys():
        if borger_values[sign] not in OAkk_values.keys(): OAkk_values[borger_values[sign]] = []
        OAkk_values[borger_values[sign]].append(
            {
            'freq':1,
            'type':'Syllabogram',
            'value':sign
            })
    else:
        print('Value ', sign, ' not found.')

# Write json file
path = os.path.dirname(os.path.dirname(__file__)) + '/values_oakk.json'
with open(path, 'w', encoding='utf8') as fp:
    json.dump(OAkk_values, fp, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)