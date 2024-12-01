# the Python request module is an HTTP library that enables developers to send HTTP request in python. This module enables you to send HTTP request using Python code and makes it possible to interact with APIs and web services

from urllib import response
import requests # type: ignore



url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":'foo',
    "body":'bar',
    "userId":1,
}

headers={
    'Content-type':'application/json;charset=UTF-8'
}
response=requests.post(url,headers=headers,json=data)