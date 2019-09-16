# This file is for pulling the data from
# the AbB to generate json file
# with values and frequencies.

import os, re, json, unicodedata, operator
from string import printable

# The lists for each sign type
all_determinatives = list()
all_logograms = list()
all_syllabograms = list()

possible_determinatives = ['diš', 'd', 'i', 'uru', 'lu2', 'lú', 'giš', 'id2', 'íd', 'munus', 'tug2', 'túg', 'kuš',
                           'ku6', 'ku₆', 'te', 'gi', 'na4', 'na₄', 'urudu', 'u2', 'ú', 'iti', 'dug', 'uzu', 'im', 'udu',
                           'kur', 'ki', 'sar', 'mušen', 'ḫi.a']

def normalize(string):
    accent_acute = u'\u0301'
    accent_grave = u'\u0300'
    allowed_characters = printable + 'ššḫṣṣṭṭ'

    # Decomp unicode
    combined = unicodedata.normalize('NFC', string.lower().strip())

    standardized_combined = ''
    for ch in combined:
        standardized_combined += replace_chars(ch)

    # Decompose the string so we can remove combining chars
    decomp = unicodedata.normalize('NFD', standardized_combined)

    # Append arabic numerals when values contain accents
    if accent_acute in decomp:
        decomp += '2'
    elif accent_grave in decomp:
        decomp += '3'

    # Remove accents but let h be ḫ
    return ''.join(c for c in unicodedata.normalize('NFD', decomp)
                   if c in allowed_characters).replace('h', 'ḫ').replace('š', 'š').replace('ṣ', 'ṣ').replace('ṭ', 'ṭ')

# Replace subscripts and enforce ḫ
# The subscript 'ₓ' is used in signlist.json, so it need not be replaced.
def replace_chars(char):
    char_map = {"h":"ḫ", "₀": "0", "₁": "1", "₂":"2", "₃":"3", "₄":"4", "₅":"5", "₆":"6", "₇":"7", "₈":"8", "₉":"9"}
    if char in char_map:
        return char_map[char]
    else:
        return char

# Take sign and add it to the right list
def add_signs(sign):

    # Upper case is logogram
    if sign == 'ḪIA':
        all_logograms.append('ḫi.a')
    elif sign.isupper():
        all_logograms.append(normalize(sign).strip())
    # Number is logogram
    elif sign.isnumeric():
        all_logograms.append(normalize(sign).strip())
    # Lower case is syllabogram
    elif sign.islower():
        all_syllabograms.append(normalize(sign).strip())
    # Fraction is logogram
    elif re.match(r"\d\/\d", sign):
        all_logograms.append(normalize(sign).strip())
    # A few weirdos
    elif sign in ['GUBｘ', 'LAḪｘ', 'GANAtenû', 'GURｘ']:
        all_syllabograms.append(sign.strip())
    # Blanks and 'luNU' and 'Da' (once each) which I don't know where they came from
    else:
        pass

# Open file with the 53169 lines in all 14 AbB volumes
path = os.path.dirname(os.path.dirname( __file__ )) + '/AbB 1–14.txt'
with open(path) as words_file:
    lines = words_file.read().splitlines()

for line in lines:
    # Get rid of the letter and line number
    line = line.split('\t')[1]

    # Clear out comments within the lines in the Czech data, contained between & and $
    if '&' in line:
        split_ampersand = line.split('&')
        split_dollar = split_ampersand[1].split('$')
        line = (split_ampersand[0].rstrip() + split_dollar[1]).rstrip()

    # Clear out lines that are just comments
    if line in ['(ligne effacée)', '[unbrauchbar]', '[does not exist anymore]', '[all the rest of the tablet uninscribed]',
                '[15 lignes illisibles]', '[illisible]', '[anépigraphe]']: line = 'x'

    # Get rid of o… and dashes marking new line (but not fractions or alternatives.
    # 30? is an inconsistency in the Czech data.
    char_map = {"o":"x", "…":"x", "\'":"ʾ", "//-":"-", "/-":"-", "-/":"-", " // ":" ", " / ":" ", "30?":"30"}
    for char in char_map: line = line.replace(char, char_map[char])

    # Special chars left in:
    #   û: twice in KA*GANAtenû-GUR₇
    #   h: data is inconsitent with ḫ/h
    #   <>(){}?x

    # Clear out brackets
    delete_brackets = "[]⌈⌉⸢⸣⌈⌉"
    for char in delete_brackets:
        if char in line: line = line.replace(char, "")

    # Get ḪI.A and HI.A and make them ḪIA so they are not split up by the .
    if 'ḪI.A' in line: line = line.replace('HI.A', 'ḪIA')
    if 'HI.A' in line: line = line.replace('HI.A', 'ḪIA')

    # Extract determinatives in parentheses
    # Things in parenthesis that are not determinatives, will be deleted at this point
    for i in re.findall(r'\([^()]*\)', line):
        if i[1:-1].lower() in possible_determinatives:
            all_determinatives.append(normalize(i[1:-1]).lower())
            line = line.replace(i, ' ')

    # The system for marking mistakes/emendations is mixed up.
    # So clear out all signs in {} <> ≤≥. Replace double brackets so it works.
    line = re.sub(r'\{.*?\}', '', line)
    line = re.sub(r'\<.*?\>', ' ', line.replace('<<', '<').replace('>>', '>'))
    line = re.sub(r'\≤.*?\≥', '', line.replace('≤≤', '≤').replace('≥≥', '≥'))

    # Split into signs. The delimiters are -*+,._× and space. Also () that are left.
    for sign in re.split('-|\*|\+|,|\.|_|×|\s|\(|\)', line):
        if any(['%' in sign, '/' in sign, '?' in sign, '!' in sign, 'x' in sign]): sign = ''
        if '(' in sign: sign = sign.replace('(', '')
        if ')' in sign: sign = sign.replace(')', '')

        # Split up logograms marked with :
        if ':' in sign:
            for each in sign.split(':'):
                if each.lower() in possible_determinatives:
                    all_determinatives.append(normalize(each).lower())
                else:
                    add_signs(each)
        else:
            add_signs(sign)



### Associate the values with Borger numbers and generate json

# Create a dict "borger_values" with "value":"borger_number"
borger_values = {}
path = os.path.dirname(os.path.dirname(__file__)) + '/signlist.json'
with open(path) as json_file: data = json.load(json_file)
for record in data.keys():
    for value in data[record]['values']:
        borger_values[value.replace('h', 'ḫ')] = record

# Create a dict "OB_freqs" with borger#, value, type, and frequency
OB_freqs = {}

# Look for borger_value for every sign
for det in set(all_determinatives):
    if det in borger_values.keys():
        if borger_values[det] not in OB_freqs.keys(): OB_freqs[borger_values[det]] = []
        OB_freqs[borger_values[det]].append({
            'freq':all_determinatives.count(det),
            'type':'Determinative',
            'value':det})
    else:
        pass#print('Determinative ', det, ' not found.')

for log in set(all_logograms):
    if log in borger_values.keys():
        if borger_values[log] not in OB_freqs.keys(): OB_freqs[borger_values[log]] = []
        OB_freqs[borger_values[log]].append({
            'freq':all_logograms.count(log),
            'type':'Logogram',
            'value':log})
    else:
        pass#print('Logogram ', log, ' not found.')

for syl in set(all_syllabograms):
    if syl in borger_values.keys():
        if borger_values[syl] not in OB_freqs.keys(): OB_freqs[borger_values[syl]] = []
        OB_freqs[borger_values[syl]].append({
            'freq':all_syllabograms.count(syl),
            'type':'Syllabogram',
            'value':syl})
    else:
        pass#print('Syllabogram ', syl, ' not found.')

# Write json file
path = os.path.dirname(os.path.dirname(__file__)) + '/freq_ob.json'
with open(path, 'w', encoding='utf8') as fp:
    json.dump(OB_freqs, fp, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)