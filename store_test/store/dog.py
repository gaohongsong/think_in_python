# -*- coding: utf-8 -*-
from .base import BaseStore


class Dog(BaseStore):

    def eat(self, food):
        print 'dog is eat {}'.format(food)

    def run(self):
        print 'dog is running'
