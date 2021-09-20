import os
from flask import Flask, render_template, request, redirect
import cognitive_face as CF

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        if "file" in request.files:
            upload_folder="./static/uploads"
            file=request.files["file"]
            file.save(os.path.join(upload_folder,file.filename))
            KEY = '95a2788553074bc3b65fcac0b4f06446'  # Replace with a valid Subscription Key here.
            CF.Key.set(KEY)
            BASE_URL = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
            CF.BaseUrl.set(BASE_URL)
            img_url = './static/uploads/{}'.format(file.filename)
            result = CF.face.detect(img_url,attributes="age,gender,emotion")

            data={
                "file_name":file.filename,
                "your-age":result[0]["faceAttributes"]["age"]
            }
            return render_template("result.html",data=data)
        else:
            render_template("index.html")

if __name__ == '__main__':
    app.run()