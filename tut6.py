import requests

r = requests.delete('https://httpbin.org/delete', data ={'key':'value'})

print(r) #status
print(r.content) #content of the page