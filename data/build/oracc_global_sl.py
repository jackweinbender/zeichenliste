import json, os

# The structure of json_signs:
#   type, project, source, license, license-url, more-info, UTC-timestamp, signs, index
#   signs is dict of
#       sign : possible_keys (+ var if it is just a sign variant)

possible_keys = ['gdl', 'utf8', 'hex', 'values', 'uphase',
                     'uname', 'n', 'v', 'pname', 'deprecated', 'uncertain', 'lang', 'unote']
values_to_signs = {}    # dictionary of every "value" :: "sign"
sign_to_values = {}     # dictionary of every "sign" :: ["value1", "value2"...]

def get_signs_from_json()
    path = os.path.dirname(os.path.dirname( __file__ )) + '/oracc_global_sl.json'
    with open(path) as signs_file:
        json_signs = json.load(signs_file)

def populate_dicts()
    for value in json_signs['index']:
        sign = json_signs['index'][value]
        values_to_signs[value] = json_signs['index'][value]
        if sign in sign_to_values:
            sign_to_values[sign].append(value)
        else:
            sign_to_values[sign] = [value]

get_signs_from_json()
populate_dicts()