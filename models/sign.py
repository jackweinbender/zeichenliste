class Sign:
    def __init__(self, row_dict):

        vals = row_dict['values'].split(';')
        unicd = row_dict['unicode_value'].split()[1:]

        self.oracc_name     = row_dict['oracc_name']
        self.unicode_name   = row_dict['unicode_name']
        self.values         = [v.strip() for v in vals]
        self.borger_id      = row_dict['borger_id']
        self.borger_name    = row_dict['borger_name']
        self.labat_id       = row_dict['labat_id']
        self.labat_name     = row_dict['labat_name']
        self.huehnergard_id = row_dict['huehnergard_id']
        self.deimel_id      = row_dict['deimel_id']
        self.mittermayer_id = row_dict['mittermayer_id']
        self.hethzl_id      = row_dict['hethzl_id']
        self.unicode_value  = ''.join(unicd)
        # self.hinke_id = row_dict['hinke_id']
        # self.clay_id = row_dict['clay_id']
        # self.ranke_id = row_dict['ranke_id']