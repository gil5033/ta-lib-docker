import os
import ccxt
import time

# Note: Need to have environment variables set.

accounts = [
    {
        'id':     'coinbasepro',
        'apiKey': os.environ['CBPRO_API_KEY'],
        'secret': os.environ['CBPRO_SECRET'],
        'password': os.environ['CBPRO_PASSWORD'],
        'symbols': ['BTCUSD'],
    },
]

for account in accounts:
    print("==========")
    print(account['id'])

    exchange_class = getattr(ccxt, account['id'])
    opts = {
        'apiKey': account['apiKey'],
        'secret': account['secret']
    }
    if 'password' in account:
        opts['password'] = account['password']
    exchange = exchange_class(opts)

    #print(dir(exchange))
    #continue

    if 'test' in account and account['test'] == True and 'test' in exchange.urls:
        exchange.urls['api'] = exchange.urls['test']

    balance = exchange.fetch_balance()
    print('balance', balance)

    try:
        tickers = exchange.fetch_tickers()
        print('tickers', tickers)
    except Exception as e:
        print(e)

    markets = exchange.load_markets()
    symbols = []
    for symbol in markets:
        symbols.append(symbol)

    print (exchange.id, symbols)

    for symbol in account['symbols']:
        orders = exchange.fetchOrders()

        for order in orders:
            print(order)
