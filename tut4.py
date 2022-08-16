import requests

r = requests.patch('https://httpbin.org/patch', data ={'key':'value'})

print(r) #status
print(r.content) #content of the page