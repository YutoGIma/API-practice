import requests
import json

def get(isbn):
    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:{}'.format(isbn)
    response = requests.get(url)
    data = json.loads(response.text)
    try:
        data = dict(
            title = data['items'][0]['volumeInfo']['title'],
            authors = ','.join(data['items'][0]['volumeInfo']['authors']),
            publishDate = data['items'][0]['volumeInfo']['publishedDate'],
            description = data['items'][0]['volumeInfo']['description'],
            image=data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"],
        )
    except:
        data = dict(detail='指定されたISBNの本は見つかりませんでした')
    return data