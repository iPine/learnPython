
# coding: utf-8

# In[2]:


import json

def format_transaction(url,blockheight,blockhash,flag=1):
    """
    获取需要的交易属性，并将其存储成目标结构；
    难点在于输入输出地址的提取：先把一个区块内的输入(出)地址添加到列表，再将列表作为一个值赋给字典的对应键。
    当一笔交易完成后（字典结构），添加到列表中；当一个区块的交易格式完以后，返回列表变量"""
    transactions = []
    addrs = []
    with open(url,'r') as f:
        #print(type(f))
        str_json = json.loads(f.read())
        
        for attr in str_json['blocks']:
            #print(len(attr['tx']))
            if (len(attr['tx'])>10):
                txs = attr['tx'][:2]
            else:
                txs = attr['tx']
            #print(len(txs))
            
            for tx in txs:
                #注意该变量的定义位置
                trans = {}
                address_name = 'addr'
                trans['blockheight'] = blockheight
                trans['blockhash'] = blockhash
                trans['hash'] = tx['hash']
                trans['ver'] = tx['ver']
                trans['time'] = tx['time']
                trans['lock_time'] = tx['lock_time']
                trans['vin_sz'] = tx['vin_sz']
                trans['vout_sz'] = tx['vout_sz']
                trans['weight'] = tx['weight']
                trans['tx_index'] = tx['tx_index']
                #trans['double_spend'] = tx['double_spend']
                trans['size'] = tx['size']
                trans['fee'] = 0
                #trans['inputs'] = tx['inputs']
                #trans['out'] = tx['out']
                #print(trans)
                #inputs是个字典列表，对于列表中的每个元素（字典），判断是否有prev_out属性存在
                input_addrs = []
                input_values = []
                for input in tx['inputs']: 
                    if 'prev_out' in input:
                        input_addrs.append(input['prev_out']['addr'])
                        input_values.append(input['prev_out']['value'])
                        
                for input_addr in input_addrs:
                    addrs.append(input_addr)
                    
                        
                trans['input_addrs'] = input_addrs
                trans['input_values'] = input_values

                output_addrs = []
                output_values = []
                for output in tx['out']:
                    if 'addr' in output:
                        output_addrs.append(output['addr'])
                        
                        # if output['addr'] not in address.values():
                        #     address['address_name'] = output['addr']
                        
                    else:
                        output_addrs.append("")
                        
                    if 'value' in output:
                        output_values.append(output['value'])

                for output_addr in output_addrs:
                    addrs.append(output_addr)

                trans['output_addrs'] = output_addrs
                trans['output_values'] = output_values  

                # print(trans['input_addrs'])
                # print(trans['output_addrs'])    

                transactions.append(trans)

        #print(len(transactions))
        # print(addrs)
        if flag:
            return addrs
        else:
            return transactions

