import sys
import pandas as pd

header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
df = pd.read_csv('/ta/' + sys.argv[1])
print(df)
