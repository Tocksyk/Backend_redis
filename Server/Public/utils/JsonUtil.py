# -*- coding: utf-8 -*-

from datetime import date
from datetime import datetime
import json


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def object_2_json(obj):
    if obj is None:
        obj = {}
    return json.dumps(obj, cls=CJsonEncoder)


def json_2_dict(json_str):
    try:
        return json.loads(json_str)
    except Exception:
        return None
