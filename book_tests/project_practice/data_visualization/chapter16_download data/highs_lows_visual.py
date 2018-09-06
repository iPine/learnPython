
# coding: utf-8

# In[2]:



import numpy as np
from matplotlib import pyplot as plt
   

class HighsLowsVisual():
    """用于可视化最低温度和最高温度的折线"""
    
    def __init__(self,dates,highs,lows):
        self.dates = dates
        self.highs = highs
        self.lows = lows
        
    def highs_lows_visual(self):
        """可视化最高温、最低温"""
        #根据数据绘制图形
        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(self.dates,self.highs,c='red',alpha=0.5)
        #在绘制一条折线
        plt.plot(self.dates,self.lows,c='blue',alpha=0.5)
        plt.fill_between(self.dates, self.highs, self.lows, facecolor='blue', alpha=0.1)

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

        

