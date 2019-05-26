# -*- coding: utf-8 -*-

"""
为了让某个python包可配置的适配多种环境，
可以在具体环境的上层抽象一层无差异的接口（定义抽象基类base），
并在具体环境中（cat/dog）实现该接口，
最后可以通过配置及动态加载的方式，加载指定环境的接口，
从而对上层引用屏蔽了下层实现的差异化
"""
import store

if __name__ == '__main__':
    """
    # settings.py
    STORE = 'store.dog.Dog'
    # python test.py
    dog is eat meat
    dog is running    

    # settings.py
    STORE = 'store.cat.Cat'
    # python test.py
    cat is eat meat
    cat is running
    """
    store.eat('meat')
    store.run()
