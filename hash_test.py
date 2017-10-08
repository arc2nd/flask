#!/usr/bin/env python
##James Parks
##10/08/17

import os
import json
import requests

def gen_hashes(passwd=None, path=None, url=None, iters=5):
    hl = []
    for i in range(iters):
        resp = requests.post(url, {'plaintext':passwd})
        if resp.status_code == 200:
            th = resp.text[1:-2]
            hl.append(th)
        else:
            print('error generating hash: first')
    with open(path, 'w+') as fp:
        json.dump(hl, fp, indent=4, sort_keys=True)

def test_hashes(passwd=None, path=None, url=None):
    good = 0
    bad = 0
    bad_hashes = []
    with open(path, 'r') as fp:
        hl = json.load(fp)
    if hl:
        for th in hl:
            print('testing hash: {}'.format(th))
            resp = requests.post(url, {'plaintext':passwd, 'hash':th})
            if resp.status_code == 200:
                ch = resp.text[1:-2]
                if th == ch:
                    good += 1
                else:
                    bad += 1
                    bad_hashes.append(th)
                    print('hash does not match\n')
            else:
                'error gernerating hash: check\n'
    else:
        print('error reading stored hashes')
    print('good hashes: {}\nbad hashes: {}\n'.format(good, bad))

if __name__ == '__main__':
    gen_hashes(passwd='thisisatest', path='/home/james/Desktop/hashes.json', url='http://localhost:5002/crypt', iters=100)
    test_hashes(passwd='thisisatest', path='/home/james/Desktop/hashes.json', url='http://localhost:5002/crypt')



