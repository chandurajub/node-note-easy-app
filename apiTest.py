#!/usr/bin/python3

import requests
import sys

response = requests.get("http://localhost:3000/")

if response.status_code == 200 :
    print("Success")
    sys.exit()
else:
    print("Fail")
    sys.exit(1)