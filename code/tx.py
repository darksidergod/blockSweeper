import json
import requests
import json
import time

api_tx = "https://api.blockcypher.com/v1/eth/main/txs"
api_block="https://api.blockcypher.com/v1/eth/main/blocks/b35265965f6f14c5d692b2030922fce53067fc0e9d8c8490c31d4ecd3e46500c"
while 1:
    unconfirmed_tx=(requests.get(api_tx)).content
    print(unconfirmed_tx)
    time.sleep(2)

    









