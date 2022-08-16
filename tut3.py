import requests

r = requests.put('https://httpbin.org/put', data ={'key':'value'})

print(r) #status
print(r.content) #content of the page