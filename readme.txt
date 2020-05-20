Docker image for using python libraries (like TA-lib and ccxt). If on linux (or possibly a mac), you may not need this docker image
as you can just create a python virtual environment and just "pip install" these libraries. Just trying to make it easy
for people to get started with python-based trading/analysis.

See https://mrjbq7.github.io/ta-lib/ for more info on TA-lib.
See https://github.com/ccxt/ccxt/wiki/Manual for more info on CCXT.

# If you want to build this container from the Dockerfile, run this: (most people will not need to do this step)
docker build -t ta-lib-docker:latest .
# or "make build"
# Note: You may need "sudo" before the docker command.

# You can run your local scripts like this:
# (which will volume mount the current directory as "/ta" on the docker container)
docker run --rm -it -v $(pwd):/ta mkinney/ta-lib-docker python /ta/one.py

# Or like this:
docker run --rm -it -e "CBPRO_API_KEY=$CBPRO_API_KEY" -e "CBPRO_SECRET=$CBPRO_SECRET" -e "CBPRO_PASSWORD=$CBPRO_PASSWORD" -v $(pwd):/ta mkinney/ta-lib-docker python /ta/cbpro_openorders.py

# to make this easier you can simply do this:
./run cbpro_openorders.py

# Example how to download AAPL prices from Yahoo Finance:
# (see https://pypi.org/project/yfinance/ for more options from yfinance lib)
./run yahoo_aapl.py
[*********************100%***********************]  1 of 1 completed
                  Open        High         Low       Close   Adj Close    Volume
Date
2019-01-02  154.889999  158.850006  154.229996  157.919998  154.794983  37039700
2019-01-03  143.979996  145.720001  142.000000  142.190002  139.376251  91312200
2019-01-04  144.529999  148.550003  143.800003  148.259995  145.326126  58607100
2019-01-07  148.699997  148.830002  145.899994  147.929993  145.002686  54777800
2019-01-08  149.559998  151.820007  148.520004  150.750000  147.766861  41025300
...                ...         ...         ...         ...         ...       ...
2019-12-19  279.500000  281.179993  278.950012  280.019989  278.602814  24592300
2019-12-20  282.230011  282.649994  278.559998  279.440002  278.025757  68994500
2019-12-23  280.529999  284.250000  280.369995  284.000000  282.562683  24643000
2019-12-24  284.690002  284.890015  282.920013  284.269989  282.831299  12119700
2019-12-26  284.820007  289.980011  284.700012  289.910004  288.442780  23280300

[249 rows x 6 columns]
# There should be an image called yahoo.aapl.png in this directory.


# Want some Crypto data? Check out this really cool script:
./run download_data.py -s ETH/USD -e coinbasepro
# This created this file: coinbasepro-ETHUSD-1d.csv


# Now you can read it back into a panda like this:
./run data_analyze.py coinbasepro-ETHUSD-1d.csv
         Timestamp    Open    High     Low   Close         Volume
0    1564099200000  219.29  222.12  212.69  219.35   75266.416623
1    1564185600000  219.42  224.14  202.46  207.11  130620.902611
2    1564272000000  207.11  213.98  197.00  211.50   81987.963835
3    1564358400000  211.50  215.31  205.70  210.73   93192.251443
4    1564444800000  210.70  214.56  204.00  209.83   55786.220075
..             ...     ...     ...     ...     ...            ...
295  1589587200000  194.66  203.36  193.24  200.53   89046.632384
296  1589673600000  200.50  210.00  199.10  207.05  114512.310561
297  1589760000000  207.05  216.99  206.99  214.97  163043.280967
298  1589846400000  214.97  215.84  209.22  214.71   98803.929453
299  1589932800000  214.80  214.97  213.76  214.18    2578.691922

[300 rows x 6 columns]
# This will create a data_analyze.png.
