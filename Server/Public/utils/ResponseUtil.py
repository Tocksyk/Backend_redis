# -*- coding: utf-8 -*-

from __future__ import absolute_import
from app.utils import JsonUtil
import flask


def standard_response(success, data):
    rst = {}
    rst['success'] = success
    rst['data'] = data
    return JsonUtil.object_2_json(rst)

def render_template(*args, **kwargs):
    return flask.render_template(*args, **kwargs)
