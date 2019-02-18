# This file is for pulling the data down from 
# Google Docs and generating the data files that 
# we use to power this thing.

import os

# Credentials from environment variables
CLIENT_ID       = os.environ.get('CLIENT_ID')
CLIENT_SECRET   = os.environ.get('CLIENT_SECRET')