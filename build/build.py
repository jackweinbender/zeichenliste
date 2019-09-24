# This file is for pulling the data down from 
# Google Docs and generating the data files that 
# we use to power this thing.

import requests, json, os, re
from collections import defaultdict
from models.sign import Sign
from models.sign_value import SignValue
from models.normalizer import Normalizer

def cleanup(d):
    d['oracc_name'] = d['oracc_name'][1:]

    for k,v in d.items():
        d[k] = v.strip()

    return d

def get_spreadsheet():
    # Spreadsheet details
    SPREADSHEET_ID = '1H3OsWtoybznhHtFzSxamPzEvCoQGOhM8sJXYOrNtsgw'
    URL = f'https://spreadsheets.google.com/feeds/list/{SPREADSHEET_ID}/od6/public/values?alt=json'

    # Get the data
    data = requests.get(URL).json()
    # Drill down to the stuff we care about (Rows is a LIST)
    rows = data['feed']['entry']

    # Dump the latest sheet into the test data so we know we don't break anything
    with open('test/data/sheets-cache.json', 'w') as outfile:
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
        
def get_ogsl():

    with open('data/signlist.json', 'w') as outfile:
        json.dump(signlist, outfile, ensure_ascii=False, sort_keys=True, indent=4)

    with open('data/search_index.json', 'w') as outfile:
        json.dump(index, outfile, ensure_ascii=False, sort_keys=True, indent=4)

def pull_ogsl():

    ##  Live version: pulls ogsl from Oracc on GitHub
    response = requests.get('https://raw.githubusercontent.com/oracc/ogsl/master/00lib/ogsl.asl')
    lines = response.text.splitlines()

    ##  Static version: if the url doesn't work, here is the backup as of 9/23/2019
    #   path = os.path.dirname(os.path.dirname(__file__)) + '/data/ogsl_backup.txt'
    #   with open(path) as file: lines = file.readlines()

    # Remove new line from every item
    ogsl = map(str.strip, lines)

    return list(ogsl)

def split_ogsl_into_signs(file):

    # Break into signs
    sign_breaks = [i for i in range(len(file)) if file[i][0:5] in ['@sign', '@nosi']]
    split_signs = [file[i: j] for i, j in zip([0] + sign_breaks, sign_breaks +
               ([len(file)] if sign_breaks[-1] != len(file) else []))]

    # Remove empty lines
    all_signs = list()
    for sign in split_signs:
        # Remove the final line '@end sign'
        drop_end = sign[:-1]
        # Clear out newlines
        all_signs.append(list(filter(None, drop_end)))
    all_signs = filter(None, all_signs)

    # Make lines into dicts
    all_signs_formatted = list()
    for sign in all_signs:
        all_signs_formatted.append(format_signs(sign))

    # Dump all signs as json
    #path = os.path.dirname(os.path.dirname(__file__)) + '/data/ogsl.json'
    #with open(path, 'w') as outfile:
    #    json.dump(signlist, outfile, ensure_ascii=False, sort_keys=True, indent=4)

def format_signs(sign_as_list):

    sign = dict()
    list_fields = ['values', 'values_insecure', 'values_abandoned', 'sign_lists',
                   'forms', 'notes', 'inotes', 'literature']

    for list_field in list_fields:
        sign[list_field] = list()

    # Split off 'forms'
    forms_begin = [i for i in range(len(sign_as_list)) if sign_as_list[i][0:5] == '@form']

    if len(forms_begin) != 0:
        sign['forms'] = sign_as_list[forms_begin[0]:-1]
        sign_as_list = sign_as_list[0:forms_begin[0]]

    # Populate dict with the fields not in forms
    keys = list()
    for line in sign_as_list:
        key = line[0:line.expandtabs().find(' ')].strip()
        value = line[len(key):].strip()
        if key in ['@sign', '@nosign']:         # Two types of sign: sign/nosign
            sign['type'] = key[1:]
            sign['oracc_name'] = value
        elif key == '@list':
            m = re.search("\d", value)
            list_name = value[0:m.start()]
            list_val = value[m.start():]
            sign['sign_lists'].append({list_name:list_val})
        elif key == '@v': sign['values'].append(value)
        elif key == '@v?': sign['values_insecure'].append(value)
        elif key == '@v-': sign['values_abandoned'].append(value)
        elif key == '@note': sign['notes'].append(value)
        elif key == '@inote': sign['inotes'].append(value)
        elif key == '@lit': sign['literature'].append(value)
        elif key == '@uphase': sign['uphase'] = value
        elif key == '@uname': sign['uname'] = value
        elif key == '@ucode': sign['ucode'] = value
        elif key == '@pname': sign['ucode'] = value
        elif key == '@end': pass
        else:
            # Remaining keys (13 times): #ša₁₈, @note:, #@ucode, @inote:, #, @unote, #inote, @not, #Molina, @fake
            # @fake (7 times) are PN, GN, ON, etc.
            pass

    return sign

# Pull the oracc list and split ogsl into signs
split_ogsl_into_signs(pull_ogsl())