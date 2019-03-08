class Sign:
    def __init__(self, row_dict):
        self.oracc_name     = row_dict['oracc_name']
        self.unicode_name   = row_dict['unicode_name']
        self.values         = row_dict['values']
        self.borger_id      = row_dict['borger_id']
        self.borger_name    = row_dict['borger_name']
        self.labat_id       = row_dict['labat_id']
        self.labat_name     = row_dict['labat_name']
        self.huehnergard_id = row_dict['huehnergard_id']
        self.deimel_id      = row_dict['deimel_id']
        self.mittermayer_id = row_dict['mittermayer_id']
        self.hethzl_id      = row_dict['hethzl_id']
        self.unicode_value  = row_dict['unicode_value']
        # self.hinke_id = row_dict['hinke_id']
        # self.clay_id = row_dict['clay_id']
        # self.ranke_id = row_dict['ranke_id']
        
    def from_sheets(sheets_row):

        sign = {}

        vals = sheets_row['values'].split(';')
        unicd = sheets_row['unicode_value'].split()[1:]

        sign['oracc_name']     = sheets_row['oracc_name']
        sign['unicode_name']   = sheets_row['unicode_name']
        sign['values']         = [v.strip() for v in vals if v.strip() != '']
        sign['borger_id']      = sheets_row['borger_id']
        sign['borger_name']    = sheets_row['borger_name']
        sign['labat_id']       = sheets_row['labat_id']
        sign['labat_name']     = sheets_row['labat_name']
        sign['huehnergard_id'] = sheets_row['huehnergard_id']
        sign['deimel_id']      = sheets_row['deimel_id']
        sign['mittermayer_id'] = sheets_row['mittermayer_id']
        sign['hethzl_id']      = sheets_row['hethzl_id']
        sign['unicode_value']  = ''.join(unicd)

        return Sign(sign)