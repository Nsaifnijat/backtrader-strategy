# -*- coding: utf-8 -*-
#if you want your own data, go to finance.yahoo and download data from historical data
#pip install backtrader
import backtrader
import datetime
from backtraderfunctions import TestStrategy
import matplotlib

cerebro=backtrader.Cerebro()

cerebro.broker.set_cash(1000000)

#feed data
data=backtrader.feeds.YahooFinanceCSVData(
    dataname='dailydata.csv',
    #start date
    fromdate=datetime.datetime(2006,1,1),
    #end date
    todate=datetime.datetime(2006,12,31),
    reversed=False)
#to check if data is connected
cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)
cerebro.addsizer(backtrader.sizers.FixedSize, stake=10000)

print('Starting Balance:%.2f' %cerebro.broker.getvalue())

cerebro.run()

print('final Balance:%.2f' %cerebro.broker.getvalue())

cerebro.plot()