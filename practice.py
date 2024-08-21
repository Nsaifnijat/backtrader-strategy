# -*- coding: utf-8 -*-

import backtrader as bt
import backtrader.analyzers as btanalyzers
import matplotlib
from datetime import datetime

class Macrossover(bt.Strategy):
    
    
    def __init__(self):
        
        ma_fast=bt.ind.SMA(period=10)
        ma_slow=bt.ind.SMA(period=50)
        self.crossover=bt.ind.CrossOver(ma_fast,ma_slow)
        self.rsi=bt.talib.RSI(self.datas[0].close,timeperiod=14)
        self.EMA=bt.talib.EMA(self.datas[0].close,timeperiod=200)
        self.rsibt=bt.indicators.RSI(self.datas[0])
        self.candle=bt.talib.CDLENGULFING(self.datas[0].open,self.datas[0].high,self.datas[0].low,self.datas[0].close)
        print(self.rsi)
    def next(self):
        
        if not self.position:
            if self.datas[0].close>self.EMA & self.rsi>50:
                if self.candle:
                    self.buy()
            elif self.rsi<50:
                
                self.close()
        print(self.rsi)        
cerebro=bt.Cerebro()

data=bt.feeds.YahooFinanceCSVData(dataname='dailydata.csv',
                               fromdate=datetime(2007,1,1),
                               todate=datetime(2013, 2, 2),
                               reversed=False)

cerebro.adddata(data)
cerebro.addstrategy(Macrossover)

#cerebro.broker.setcash(1000000)

cerebro.addsizer(bt.sizers.PercentSizer, percents=5)



cerebro.run()

cerebro.broker.getvalue()



print(bt.talib.SMA.__doc__)

print('SMA:', bt.talib.MA_Type.SMA)
print('T3:', bt.talib.MA_Type.T3)






'''
   def next(self):
        
        if not self.position:
            if self.crossover>0:
                
                self.buy()
            elif self.crossover<0:
                
                self.close()

'''

