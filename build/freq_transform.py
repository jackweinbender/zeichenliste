import os, re, json, unicodedata, operator
# from string import printable

# Open file with the 196 syllabic values in OAkk

files = ['ebla', 'na', 'nb', 'oakk', 'ob']

for f in files:
    output = []
    path = os.path.dirname(__file__) + '/legacy_data/freq_' + f + '.json'
    with open(path) as data:  
            freq_data = json.load(data)

    for borger_id in freq_data.keys():
        freq_list = freq_data[borger_id]
        for freq in freq_list:
            freq['borger_id'] = int(borger_id)
            freq['corpus'] = f
            freq['freq'] = int(freq['freq'])
            output.append(freq)
    
    with open('data/freq_' + f + '.json', 'w', encoding='utf8') as out:
        json.dump(output, out, indent=2, ensure_ascii=False)