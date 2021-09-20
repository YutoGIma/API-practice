import requests
import json

url="https://api.opendata.go.jp/mhlw/death-cases?apikey=qJW5j4E7AFnvosG5wcIvW49GLQDqN1SU"
requestHeaders = {
    "Accept": "application/json"
  }

response=requests.get(url,headers=requestHeaders)

data=json.loads(response.text)
print(data)
