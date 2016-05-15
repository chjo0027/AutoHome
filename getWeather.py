# -*- coding: utf-8 -*-
import requests
import json
def getWeather():
    url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22billdal%22)%20and%20u%20%3D%20'c'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    respone = requests.get(url)
    data = respone.json()
    viewData =  data["query"]["results"]["channel"]["location"]["city"]+', '
    viewData += data["query"]["results"]["channel"]["location"]["country"]
    viewData += '\n'+data["query"]["results"]["channel"]["item"]["condition"]["temp"]+u"\u00B0"+'C'
    viewData += ', '+data["query"]["results"]["channel"]["item"]["condition"]["text"]
    viewData += '\n'+data["query"]["results"]["channel"]["wind"]["speed"]+' km/h'
    return viewData