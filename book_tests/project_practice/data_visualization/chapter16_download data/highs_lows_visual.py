
# coding: utf-8

# In[2]:



import numpy as np
from matplotlib import pyplot as plt
   

class HighsLowsVisual():
    """用于可视化最低温度和最高温度的折线
        可绘制一个数据，也可绘制两个数据
    """
    
    def __init__(self,dates,highs,lows,dates1='',highs1='',lows1=''):
        self.dates = dates
        self.highs = highs
        self.lows = lows
        self.dates1 = dates1
        self.highs1 = highs1
        self.lows1 = lows1
        
    def highs_lows_visual(self):
        """可视化最高温、最低温"""
        #根据数据绘制图形
        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(self.dates,self.highs,c='red',alpha=0.5)
        #再绘制一条折线
        plt.plot(self.dates,self.lows,c='blue',alpha=0.5)
        plt.fill_between(self.dates, self.highs, self.lows, facecolor='blue', alpha=0.3)

        #另一个数据
        if self.dates1:
            plt.plot(self.dates1,self.highs1,c='yellow',alpha=0.5)
            plt.plot(self.dates1,self.lows1,c='green',alpha=0.5)
            plt.fill_between(self.dates1, self.highs1, self.lows1, facecolor='blue', alpha=0.3)

        #设置图形格式
        title = "Daily high and low temperatures - 2014"
        plt.title(title, fontsize=24) 
        plt.xlabel('', fontsize=16)
        #调用了 fig.autofmt_xdate() 来绘制斜的日期标签，以免它们彼此重叠
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        #设置Y轴刻度
        my_y_ticks = np.arange(0,120,step=10)
        plt.yticks(my_y_ticks)

        plt.show()

        

