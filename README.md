## 重拾Python

&ensp;&ensp;希望通过笔记的方式，能进一步学习Python，掌握一些经典的编程实践方法，梳理自己工作中的一些Python
编程技巧，为一些常规问题积攒经验。

## 1. 如何让某个python包优雅的适配各种环境？

参考：[store](https://github.com/gmaclinuxer/think_in_python/blob/master/store_test.py#L12)

> 为了让某个python包可配置的适配多种环境，
可以在具体环境的上层抽象一层无差异的接口（定义抽象基类base），
并在具体环境中（cat/dog）实现该接口，
最后可以通过配置及动态加载的方式，加载指定环境的接口，
从而对上层应用(store_test)屏蔽下层实现的差异化细节
