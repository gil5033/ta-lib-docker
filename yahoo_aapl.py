# example from: https://blog.quantinsti.com/install-ta-lib-python/
import talib as ta
import matplotlib.pyplot as plt
plt.style.use('bmh')
import yfinance as yf
aapl = yf.download('AAPL', '2019-1-1','2019-12-27')
# If you want to see data
print(aapl)

aapl['Simple MA'] = ta.SMA(aapl['Close'],14)
aapl['EMA'] = ta.EMA(aapl['Close'], timeperiod = 14)

# Plot
aapl[['Close','Simple MA','EMA']].plot(figsize=(15,15))
# Since we're not really on the container, we need to save the plot to an image.
#plt.show()
plt.savefig('/ta/yahoo_aapl.png')
