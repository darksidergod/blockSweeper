import json
import requests
import json
import time
import re
import os
import itertools
import operator

api_tx = "https://api.blockcypher.com/v1/eth/main/txs"
api_block="https://api.blockcypher.com/v1/eth/main/blocks/b35265965f6f14c5d692b2030922fce53067fc0e9d8c8490c31d4ecd3e46500c"

tx_dataMap={}

while 1:
        data=requests.get(api_tx).content
        tx_hashes=re.findall('"hash": "\w*"+', data)
        gas_limits=re.findall('gas_limit": \d*', data)
        gas_prices=re.findall('gas_price": \d*', data)
        
        for (a, b, c) in zip(tx_hashes, gas_limits, gas_prices):   
            ans=int(b[12:])*int(c[12:])
            tx_dataMap[a]=ans
        
    
        sorted_tx_dataMap=sorted(tx_dataMap.items(), key=operator.itemgetter(1))

        for item in sorted_tx_dataMap:
            print(item)

        time.sleep(2)

    
    

    








