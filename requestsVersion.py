#!/usr/bin/env python

import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print(r)
# print(dir(r))
print(r.text)
print(r.status_code)

r = requests.get("https://raw.githubusercontent.com/ItsOhSoQuiet/CMPUT404Lab1/master/requestsVersion.py")
print(r.text)