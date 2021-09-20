import requests
from flask import Flask, render_template
import json


app=Flask(__name__)
app.debug=True

@app.route("/")
def root():
    url="https://api.opendata.go.jp/mhlw/positive-cases?apikey=qJW5j4E7AFnvosG5wcIvW49GLQDqN1SU"
    requestHeaders = {
        "Accept": "application/json"
    }
    Response=requests.get(url,headers=requestHeaders)
    data_list=json.loads(Response.text)
    return render_template("index.html",data_list=data_list)


@app.route("/chart")
def chart():
    url="https://api.opendata.go.jp/mhlw/positive-cases?apikey=qJW5j4E7AFnvosG5wcIvW49GLQDqN1SU"
    requestHeaders = {
        "Accept": "application/json"
    }
    Response=requests.get(url,headers=requestHeaders)
    data_list=json.loads(Response.text)
    data_day=[]
    positive_list=[]
    for data in data_list:
        data_day.append(data["日付"])
        positive_list.append(data["PCR 検査陽性者数(単日)"])
    return render_template("chart.html",data_day=data_day,positive_list=positive_list)

if __name__=="__main__":
    app.run()