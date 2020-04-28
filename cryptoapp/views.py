from django.shortcuts import render
import requests
import json

def index(request):
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=REP,BTC,XRP,ETH,BCH,BSV,LTC,EOS,BNB,XTZ&tsyms=USD")
    price = json.loads(price_request.content)
    return render(request,'cryptoapp/index.html',{'api':api,'price':price})

def search(request):
    if request.method == "POST":
        data = request.POST['data']
        price_request_data = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ data.capitalize() +"&tsyms=USD")
        price_data = json.loads(price_request_data.content)
        return render(request,'cryptoapp/search.html',{'price_data':price_data})

    else:
        display_something = "Search your crypto currency above"    
        return render(request,'cryptoapp/search.html',{'display_something':display_something})

