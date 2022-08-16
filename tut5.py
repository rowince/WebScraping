import requests

r = requests.head('https://httpbin.org/', data={'key': 'value'})

print(r)  # status
print(r.headers)  # header
print(r.content)  # content of the page
