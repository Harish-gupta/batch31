import requests
resp = requests.post("http://localhost:5000/",data={'id':8,'name':'book8'})
print resp
resp = requests.get("http://localhost:5000/books")
print resp.json()

