import requests
import json

r = requests.get('https://cascades.dev/api')
jsonObject = json.loads(r.text)

print(jsonObject["quote"])