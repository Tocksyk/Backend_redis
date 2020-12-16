# -*- coding: utf-8 -*-

import hashlib


def md5_salt(s, salt="redis-monitor"):
    if s:
        return md5(s + salt)
    else:
        return ''


def md5(s):
    s = s.encode('utf-8')
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()
