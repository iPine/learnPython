## All code is used to craw data from [Blockchain](https://www.blockchain.com)  

### References 

#### 数据链接
- [Data API](api/blockchain_api)

- [Blocklist](https://www.blockchain.com/btc/blocks/1531905176688)

#### 代码使用(Jupyter nootbook)

1 . 使用`blockhash_craw.ipynb` ：获取想要爬取的比特币区块数据的哈希值

2 . 使用`blockdata_craw.ipynb` ：根据区块哈希值，在下载地址(https://blockchain.info/rawblock/$block_hash )，批量下载区块数据

3 . 使用`extract_trans_addrs.ipynb` 与 `format_transaction` : 从获取到的区块数据中，提取交易信息数据并做格式处理，以及提取交易涉及到的所有地址

4 . 使用 `addressinfo_craw.ipynb` : 根据地址字符串，在下载地址(https://blockchain.info/rawaddr/$bitcoin_address )，批量下载钱包地址包含的信息数据

5 . 使用`format_addrinfo.ipynb` : 处理下载的钱包地址数据