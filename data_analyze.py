import sys
import talib as ta
import matplotlib.pyplot as plt
import pandas as pd

header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
df = pd.read_csv('/ta/' + sys.argv[1])
# to see data
print(df)

df['Simple MA'] = ta.SMA(df['Close'],14)
df['EMA'] = ta.EMA(df['Close'], timeperiod = 14)

# Plot
df[['Close','Simple MA','EMA']].plot(figsize=(15,15))
# Since we're not really on the container, we need to save the plot to an image.
#plt.show()
plt.savefig('/ta/data_analyze.png')
