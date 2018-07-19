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