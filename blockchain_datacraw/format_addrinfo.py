
# coding: utf-8

# In[1]:


import json

def format_address(address):
    """
        处理爬取的地址信息；
        若当前地址相关的交易数多于10笔，则只保留前10笔交易
    """ 
    #print(address + '.json')
    addressinfo_list = []
    with open(address + '.json','r') as f:
        str_json = json.loads(f.read())
#         print(str_json)

        for addr in str_json['addrs']:
#             print(addr)
            addressinfo = {}
            print("该交易地址原本有的总交易数量：",len(addr['txs']))
            while (len(addr['txs'])) > 10:
                addr['txs'].pop()
            print(len(addr['txs']))
#             只保留需要的属性信息
            addressinfo['hash160'] = addr['hash160']
            addressinfo['address'] = addr['address']
            addressinfo['n_tx'] = addr['n_tx']
            addressinfo['total_received'] = addr['total_received']
            addressinfo['total_sent'] = addr['total_sent']
            addressinfo['final_balance'] = addr['final_balance']
            #开始处理交易，作为一个列表
            txs_list = []
            for tx in addr['txs']:
                txs = {}
                txs['time'] = tx['time']
                txs['size'] = tx['size']
                txs['ver'] = tx['ver']
                txs['vins'] = tx['vin_sz']
                txs['vouts'] = tx['vout_sz']
                txs['hash'] = tx['hash']
                txs['value'] = 0
                #计算当前交易金额，判断状态是转入还是转出
                #txs['value'] = 0
                for tx_in in tx['inputs']:
                    if 'prev_out' in tx_in:
                        if 'addr' in tx_in['prev_out']:
                            if addr['address'] == tx_in['prev_out']['addr']:
                                txs['state'] = 'out'
                                txs['value'] = tx_in['prev_out']['value']
                                break
                 
                if txs['value'] == 0:
                    # print(tx)
                    for tx_out in tx['out']:
                        # print(tx_out)
                        if tx_out['value'] == 0:
                            continue
                        
                        if addr['address'] == tx_out['addr']:
                            txs['state'] = 'in'
                            txs['value'] = tx_out['value'] 
                            break
                            
                
                txs_list.append(txs)
                
            addressinfo['txs'] = txs_list
            addressinfo_list.append(addressinfo)
        
        return addressinfo_list

