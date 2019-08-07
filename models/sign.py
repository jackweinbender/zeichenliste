class Sign:
    def __init__(self, row_dict):
        # We use Borger as the main ID
        self.borger_id      = row_dict['borger_id']
        self.borger_name    = row_dict['borger_name']

        # Unicode and ORACC standardized name
        self.unicode_value  = row_dict['unicode_value']
        self.unicode_name   = row_dict['unicode_name']
#Change
        # Other Names
        self.oracc_name     = row_dict['oracc_name']
        self.labat_name     = row_dict['labat_name']
        
        # The Values of the Sign
        self.values         = row_dict['values']

        # Other Signlist numbers
        self.labat_id       = row_dict['labat_id']
        self.huehnergard_id = row_dict['huehnergard_id']
        self.deimel_id      = row_dict['deimel_id']
        self.mittermayer_id = row_dict['mittermayer_id']
        self.hethzl_id      = row_dict['hethzl_id']
    
    def from_sheets_row(sheets_row):
        sign_dict = {
            'unicode_value':  sheets_row['gsx$unicode']['$t'],
            'values':         sheets_row['gsx$values']['$t'],
            'borger_id':      sheets_row['gsx$borger']['$t'],
            'borger_name':    sheets_row['gsx$borgername']['$t'],
            'oracc_name':     sheets_row['gsx$oraccname']['$t'],
            'labat_name':     sheets_row['gsx$labatname']['$t'],
            'labat_id':       sheets_row['gsx$labat']['$t'],
            'huehnergard_id': sheets_row['gsx$huehnergard']['$t'],
            'deimel_id':      sheets_row['gsx$deimel']['$t'],
            'mittermayer_id': sheets_row['gsx$mittermayer']['$t'],
            'hethzl_id':      sheets_row['gsx$hethzl']['$t'],
            'unicode_name':   sheets_row['gsx$unicodename']['$t'],
        }

        # Cleanup
        for k,v in sign_dict.items():
            sign_dict[k] = v.strip()
        
        # Munge-it #
        ## Unicode values
        unicd = sign_dict['unicode_value'].split(" & ")
        unicode_signs = [''.join(v.strip().split()[1:]) for v in unicd]
        sign_dict['unicode_value'] = '+'.join(unicode_signs)
        ## Sign Values
        values = sign_dict['values'].split(';')
        sign_dict['values'] = [v.strip() for v in values if v.strip() != '']
        ## ORACC ID
        sign_dict['oracc_name'] = sign_dict['oracc_name'][1:]
        return Sign(sign_dict)