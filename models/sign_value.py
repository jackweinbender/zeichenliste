import re

class SignValue:
    def __init__(self, value):
        self.value = value
        
    def get_keys(self):
        # https://pythex.org/?regex=%5E(%5Cd)%3F%5C(%3F(%5CD%2B)(%5Cd*)%40%3F(%5Cw)%3F%5C)%3F%24&test_string=ban2%0Abanda2%0Asutu%0A1(ban2)%0A1(ban2%40c)%0Aban2%40c%0Aban2%40v&ignorecase=0&multiline=1&dotall=0&verbose=0
        # Matches for the above REGEX must match the following
            # sutu
            # ban2
            # banda2
            # ban2@c
            # 1(ban2)
            # 1(ban2@c)
        # MATCH GROUPS
        # - 1 = prefix digit 
        # - 2 = phonetic value or non-digit alphanumerics
        # - 3 = subscript
        # - 4 = postfix (after @-symbol)
        
        expr = re.compile('^(\d\/?\d?)?\(?(\D+)(\d*)@?(\w)?\)?$')
        
        values = self.value.strip().split('-')
        value_groups = set()

        for v in values:
            match = expr.match(v.strip())
            # Just in case something doesn't match
            if not match:
                print(f'WARNING, VALUE {v} DID NOT MATCH')
                value_groups.add(v)
            else:
                value_groups.add(match.group(2))
                value_groups.add(match.group(2) + match.group(3))
        return list(value_groups)
