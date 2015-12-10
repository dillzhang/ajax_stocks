import urllib2, json



def getJSON(stockTicker):
    url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol="
    url += stockTicker
    url += "&callback=myFunction"
    
    page = urllib2.urlopen(url)
    responce = json.load(page)
    print responce.keys()
    print responce['Name']
    return responce
getPrice("AAPL")
