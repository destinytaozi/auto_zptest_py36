# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       math_func
    Description:
    Author:          destiny
    date:            2018/7/18 14:10
--------------------------------------------------------------------
    Change Activity:
                    2018/7/18 14:10
--------------------------------------------------------------------
"""
import random

__author__ = 'destiny'

class mathFunction():
    def random_pick(self,some_list,probabilities):
        x = random.uniform(0, 1)
        cumulative_probability = 0.0
        for item, item_probability in zip(some_list, probabilities):
            cumulative_probability += item_probability
            if x < cumulative_probability: break
        return item

    def random_index(self,rate):
        """随机变量的概率函数"""
        #
        # 参数rate为list<int>
        # 返回概率事件的下标索引
        start = 0
        index = 0
        randnum = random.randint(0,1)

        for index, scope in enumerate(rate):
            start += scope
            if randnum < start:
                break
        return index
mf=mathFunction()

print(mf.random_index((1,2,3,4)))