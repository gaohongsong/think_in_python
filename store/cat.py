# -*- coding: utf-8 -*-
from .base import BaseStore


class Cat(BaseStore):

    def eat(self, food):
        print 'cat is eat {}'.format(food)

    def run(self):
        print 'cat is running'
