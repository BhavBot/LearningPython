import requests

# url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=X6A2F86DSI79TGVU'
# r = requests.get(url)
# data = r.json()

# print(data)

def what(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=X6A2F86DSI79TGVU'
    r = requests.get(url)
    data = r.json()
    return data
    
thing=what("AAPL")
if thing["Global Quote"]:
    print(thing["Global Quote"]["05. price"])

thing2=what("GOOGL")
if thing2["Global Quote"]:
    print(thing2["Global Quote"]["05. price"])