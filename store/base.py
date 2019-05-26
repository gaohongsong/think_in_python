# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta


class BaseStore(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def eat(self, food):
        raise NotImplementedError()

    @abstractmethod
    def run(self):
        raise NotImplementedError()
