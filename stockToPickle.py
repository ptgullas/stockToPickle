"""
Stock to Pickle

Accepts a stock ticker as an argument
Fetches stock history from Morningstar, and saves it as a pickle file
"""
import sys
import pandas as pd
import datetime
import os.path

# the following line is a workaround to avoid the "cannot import name is_list_like error"
# due to an issue in pandas_datareader 0.6.0
# https://stackoverflow.com/questions/50394873/import-pandas-datareader-gives-importerror-cannot-import-name-is-list-like
# Remove this with p_d 0.7.0 or later
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

def getStockDF(stockTicker, start, end):
    print(f"Retrieving stock data for {stockTicker}")
    df = web.DataReader(stockTicker,"morningstar", start, end)  
    return df

def savePickle(myDF, myFileName):
    print(f"Entered savePickle. Saving to {myFileName}")
    myDF.to_pickle(myFileName)


def main():
    if len(sys.argv) < 2:
        print('usage: ./stockToPickle.py stockticker startdate enddate')
        sys.exit(1)
    elif len(sys.argv) == 2:
        myStart = "20100101"
    else:
        myStart = sys.argv[2]

    stockTicker = sys.argv[1]
    # startYear = int(myStart[0:4])
    # startMonth = int(myStart[4:6])
    # startDay = int(myStart[6:8])
    start = datetime.datetime.strptime(myStart,'%Y%m%d')
    #start = datetime.datetime(startYear,startMonth,startDay)
    end = datetime.datetime.now()
    myDF = getStockDF(stockTicker, start, end)

    myFileName = stockTicker.lower() + '_' + start.strftime("%Y%m%d") + '_' + end.strftime("%Y%m%d") + '_data.pkl'
    savePickle(myDF, myFileName)

if __name__ == '__main__':
  main()
