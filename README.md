python-upbit
============

This is an unofficial Python wrapper for the Upbit API. I am not affiliated with Upbit. Please use at your own risk.

Donation
--------

BTC: 3Lpz6PJVtvBFhBjegvT9jyhuzkJ5LAkxGY  
ETH: 0x84D433120B0Aa19B5d9124d03ecD42665c0Fd958  
BCC: 3N5BhKh5mvKWt4oYe7FEYk24iZ7Ra64f5k  
LTC: 38QsK8687QKSTthbnSZuhqeMAYWe2mgaU8  
NEO: AY6jKuD6zwePxP4S6286ykRXj7JC7eAR2W  

Installation
------------

```
pip install upbit
```

Usage
-----

```
>>> from upbit import Upbit
>>> my_upbit = Upbit(None, None)
>>> my_upbit.get_markets()
[{'market': 'KRW-BTC', 'korean_name': '비트코인', 'english_name': 'Bitcoin'}, {'market': 'KRW-DASH', 'korean_name': '대시', 'english_name': 'Dash'}, {'market': 'KRW-ETH', 'korean_name': '이더리움', 'english_name': 'Ethereum'}, {'market': 'BTC-NEO', 'korean_name': '네오', 'english_name': 'NEO'}, ...
```

```
>>> from upbit import Upbit
>>> my_upbit = Upbit('access_key', 'secret_key')
>>> my_upbit.get_assets()
[{'currency': 'KRW', 'balance': '0.59953986', 'locked': '0.0', 'avg_krw_buy_price': '0', 'modified': False}, {'currency': 'BTC', 'balance': ...
```

Reference
---------

https://docs.upbit.com/v1.0/reference

Licence
-------

The MIT License (MIT)  
Copyright (c) 2018 Seokhwan Cheon  
