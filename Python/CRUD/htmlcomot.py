import requests

resp = requests.get('http://localhost:8000/hutss')
if resp.ok:
    print (resp.text)
else:
    print ("Boo! {}".format(resp.status_code))
    print (resp.text)