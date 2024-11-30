import requests
import json

key = 'your api key from newsapi.org'

class News:
    catagory = ["business","entertainment","general","health","science","sports","technology"]
    language = "en"
    url = f"https://newsapi.org/v2/top-headlines/sources?language=en&category=business&apiKey={key}"
    def __init__(self,key,cat):
        self.key = key
        self.cat = cat

    def api(self):
        self.url = f"https://newsapi.org/v2/top-headlines/sources?language={self.language}&category={self.cat}&apiKey={self.key}"
        response = requests.get(self.url)
        return response.text

    @staticmethod
    def print_catagory():
        for idx,val in enumerate(News.catagory):
            print(f"{idx+1}) {val}")
        while True:
            if(user:=int(input('which news are you looking for: '))) <=7 and user>=1:
                return News.catagory[user-1]
            print('no such catagory!!!')


print('welcome to newsapi')
cat = News.print_catagory()
new = News(key,cat)
response = new.api()
response_dict = json.loads(response)
to_get = response_dict['sources']
for i in range(len(to_get)):
    print("============")
    print(f"Title : {to_get[i]['name']}")
    print(f"News : {to_get[i]['description']}")
    print(f"Learn more : {to_get[i]['url']}")