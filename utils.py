
import urllib2, json



def getJSON(stockTicker):
    url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol="
    url += stockTicker
    
    page = urllib2.urlopen(url)
    responce = json.load(page)
    print responce.keys()
    print responce['LastPrice']
    print responce['ChangeYTD']
    return responce
getJSON("AAPL")

def estimateReturn(stockTicker, investment):
	stockData = getJSON(stockTicker)
	origPrice = stockData['ChangeYTD']
	lastPrice = stockData['LastPrice']
	numStocks = investment * 1.0 / origPrice 
	currWorth = numStocks * lastPrice
	netProfit = currWorth - investment
	return netProfit
print estimateReturn("AAPL", 1000000)

def guessTicker(company):
	url = "http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input="
	url += company
	page = urllib2.urlopen(url)
	responce = json.load(page)
	if (len(responce) < 1):
		return "Error, Stock Ticker not found"
	return responce[0]['Symbol']
