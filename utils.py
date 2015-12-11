from os import urandom
import urllib2, json

secret_key = urandom(32)

def getJSON(stockTicker):
    url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol="
    url += stockTicker
    url += "&callback=myFunction"
    
    page = urllib2.urlopen(url)
    responce = json.load(page)
    print responce.keys()
    print responce['Name']
    return responce
getJSON("AAPL")
