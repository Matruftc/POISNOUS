import requests

url = 'https://mail.google.com/mail/u/0/#inbox'
x = requests.get(url) 

print(x.text)