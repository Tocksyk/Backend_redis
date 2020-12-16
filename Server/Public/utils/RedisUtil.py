# -*- coding: utf-8 -*-

import redis

'''
def flushall(host, port, password, db):
    r = redis.Redis(host=host, port=int(port), password=password, db=int(db))
    return r.flushdb()

def set_value(host, port, password, db, key, value, timeout=-1):
    r = redis.Redis(host=host, port=int(port), password=password, db=int(db))
    return r.setex(key, value, timeout)

def del_key(host, port, password, db, key):
    r = redis.Redis(host=host, port=int(port), password=password, db=int(db))
    return r.delete(key)
'''
def flushall(host, port, password):
    r = redis.Redis(host=host, port=int(port), password=password)
    return r.flushdb()

def set_value(host, port, password, key, value):
    r = redis.Redis(host=host, port=int(port), password=password)
    return r.set(key, value)

def del_key(host, port, password, key):
    r = redis.Redis(host=host, port=int(port), password=password)
    return r.delete(key)