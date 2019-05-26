# -*- coding: utf-8 -*-
from . import settings
from .utils import import_string

__all__ = [
    'eat',
    'run'
]

__store = None

if not __store:
    try:
        store_cls = import_string(settings.STORE)
        __store = store_cls()
    except ImportError as e:
        raise Exception("import store({}) error: {}".format(settings.STORE, e))

eat = __store.eat
run = __store.run
