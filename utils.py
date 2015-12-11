from os import urandom
import urllib2
import json

secret_key = urandom(32)


def getJSON(stockTicker):
    url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol="
    url += stockTicker
    
    page = urllib2.urlopen(url)
    responce = json.load(page)
    return responce


def getReturn(stockTicker, investment):
    information = {}
    stockData = getJSON(stockTicker)
    origPrice = stockData['ChangeYTD']
    lastPrice = stockData['LastPrice']
    numStocks = investment * 1.0 / origPrice
    currWorth = numStocks * lastPrice
    netProfit = currWorth - investment
    information['returnInfo'] = netProfit
    return information


def guessTicker(company):
    url = "http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input="
    url += company
    page = urllib2.urlopen(url)
    responce = json.load(page)
    if (len(responce) < 1):
        return "Error, Stock Ticker not found"
    return responce[0]['Symbol']


def getInfo():
    f = open("stockTicker.csv", "r")
    stocks = f.read().split("\n")
    f.close()
    information = {}
    for stock in stocks:
        stockData = getJSON(stock)
        information[stock] = stockData['LastPrice']
    return information
