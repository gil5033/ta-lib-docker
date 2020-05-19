Build docker image so you can use TA-lib using python.

See https://mrjbq7.github.io/ta-lib/

# Note: You may need "sudo" before this command.
docker build -t ta-lib-docker:latest .

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
