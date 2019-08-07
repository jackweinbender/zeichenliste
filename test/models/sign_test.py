# Tests for the App
from data.build.models.sign import Sign
import json

class TestSign:
    def test_from_sheets_row_builds_sign(self):
        """Asserts that the sheet-cache serializes to what we have in the signlist"""
        with open('test/data/sheets-cache.json') as f:
            data = json.load(f)

        with open('data/signlist.json') as zl:
            signlist = json.load(zl)

        for row in data:
            sign = Sign.from_sheets_row(row)
            expected = signlist[sign.borger_id]
            assert sign.__dict__ == expected
            
            
        