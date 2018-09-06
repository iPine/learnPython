
# coding: utf-8

# In[ ]:


import csv
from datetime import datetime

def read_file(filename):
    """从文件中读取最高气温、最低气温、日期"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [],[],[]
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError: 
                print(current_date, 'missing data')
            else: 
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    return dates,highs,lows

