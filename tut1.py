import requests

r = requests.get('https://api.github.com/users/rowince')
print(r) #it gives the status code
print(r.content) #it gives the content of the page 