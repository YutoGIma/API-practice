import requests
import json

url="https://zipcloud.ibsnet.co.jp/api/search?zipcode=9011102"

response=requests.get(url)

address=json.loads(response.text)["results"]
print(address)

message="私の住んでいるのは{}{}{}です。".format(
    address[0]["address1"],address[0]["address2"],address[0]["address3"]
)
print("私の住んでいる県は"+address[0]["address1"]+"です。")
print(message)