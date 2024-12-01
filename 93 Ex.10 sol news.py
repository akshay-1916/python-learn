import requests
import json


query=input("What type of news are you interested in?")
url=f"pest here url web"
r=requests.get(url)
news=json.loads(r.text)

for article in news["articles"]:
    print(article.title)
    print(article.description)