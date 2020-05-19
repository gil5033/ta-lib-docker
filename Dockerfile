FROM python:3

# install ta-lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/usr && \
  make && \
  make install

# install python requirements and python ta-lib wrapper
RUN git clone https://github.com/mrjbq7/ta-lib.git /ta-lib-py
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /ta-lib-py/requirements.txt
RUN cd /ta-lib-py && python setup.py install

# install some python libs
RUN pip install --no-cache-dir pandas bybit ccxt python-binance pandas-datareader matplotlib scipy yfinance

# install vim
RUN apt-get update && apt-get install -y \
  vim
