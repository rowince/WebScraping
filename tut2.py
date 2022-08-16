import requests

r = requests.post('https://httpbin.org/post', data ={'key':'value'})

print(r) #status
print(r.content) #content of the page