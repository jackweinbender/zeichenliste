import unicodedata

class Normalizer:
    
    @classmethod
    def normalize(cls, string):
        accent_acute = u'\u0301'
        accent_grave = u'\u0300'
        
        # Decomp unicode 
        combined = unicodedata.normalize('NFC', string.lower().strip())

        standardized_combined = ''
        for ch in combined:
            standardized_combined += cls._replace_chars(ch)
        
        # Decompose the string so we can remove combining chars
        decomp = unicodedata.normalize('NFD', standardized_combined)

        # Append arabic numerals when values contain accents
        if accent_acute in decomp:
            decomp += '2'
        elif accent_grave in decomp:
            decomp += '3'
        
        

        #strip all accents
        return ''.join(c for c in unicodedata.normalize('NFD', decomp)
                  if unicodedata.category(c) != 'Mn')
    
    @staticmethod
    def _replace_chars(char):
        char_map = {
            # 'ḫ': 'h',
            'š': 'sz',
            'ĝ': 'ng',
            'ŋ': 'ng',
            # 'ṣ': 's',
            # 'ṭ': 't',
            "ₓ": "x", # subscript x, replaced with lowercase
            "₀": "0",
            "₁": "1",
            "₂": "2",
            "₃": "3",
            "₄": "4",
            "₅": "5",
            "₆": "6",
            "₇": "7",
            "₈": "8",
            "₉": "9"
        }
        if char in char_map:
            return char_map[char]
        else:
            return char