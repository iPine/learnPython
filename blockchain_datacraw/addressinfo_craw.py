
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import json

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def get_addrslist():
    """只使用与展示交易相关的所有地址;
    将address.json文件里的地址存入列表待用
    """
    with open('address.json','r') as f:
        addrs = json.loads(f.read())
    #     print(addrs['address'])
        addrs_list = []
        for addr in addrs['address']:
            #剔除重复地址
            if addr['addr'] not in addrs_list:
                addrs_list.append(addr['addr'])
        return addrs_list


def addressinfo_craw(address):

    #address = '1EVzaFkkNNXq6RJh2oywwJMn8JPiq8ikDi'
    url = 'https://blockchain.info/rawaddr/' + address
    #print(url)

    html = getHTMLText(url)
    

    print('开始抓取')
    with open(address+'.json','w') as f:
        try:
        #必须要这样格式化了，方便format_address()读取json文件
            f.write('{"addrs":[')
            for line in html:
                f.write(line.strip())
            f.write(']}')

        except Exception:
            print('发生错误')

    print('抓取成功')

    
def format_address(address):
    """
        处理爬取的地址信息；
        若当前地址相关的交易数多于10笔，则只保留前10笔交易
    """ 
    #print(address + '.json')
    with open(address + '.json','r+') as f:
        str_json = json.loads(f.read())
#         print(str_json)
        for addr in str_json['addrs']:
            #print(addr)
            print("该交易地址原本有的总交易数量：",len(addr['txs']))
            while (len(addr['txs'])) > 10:
                addr['txs'].pop()
            print(len(addr['txs']))
 
    


def main():
    # addrs_list=get_addrslist()
    # addrs_new = addrs_list[:5]
    addrs_new = get_addrslist()
    print("需要提取信息的地址总数：",len(addrs_new))
    print("需要提取信息的地址：{}".format(addrs_new))

    address_list = []
    while len(addrs_new)>0:
        address = addrs_new.pop()
        print("当前正在处理的地址：",address)
        if len(address) == 34:
            print("还未处理的地址数量：",len(addrs_new))
            addressinfo_craw(address)
            format_address(address)
        else:
            print('该地址长度无效！')
            continue