import cognitive_face as CF

KEY = '95a2788553074bc3b65fcac0b4f06446'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url = 'https://pbs.twimg.com/media/E-u9iVAVgAEpv8D?format=jpg&name=large'
result = CF.face.detect(img_url,attributes="age,gender,emotion")
print(result)