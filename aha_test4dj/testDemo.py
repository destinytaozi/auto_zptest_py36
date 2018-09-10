# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       testDemo
    Description:
    Author:          destiny
    date:            2018/8/8 20:55
--------------------------------------------------------------------
    Change Activity:
                    2018/8/8 20:55
--------------------------------------------------------------------
"""
__author__ = 'destiny'




class Money:
    currency_rates = {
        '$': 1,
        '€': 0.8612,
        '¥': 6.8192,
        '￥': 110.77,
        '£': 0.7763
    }

    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

    def __repr__(self):
        return '%s%.4f' % (self.symbol, self.amount)

    def __str__(self):
        return '%s%.4f' % (self.symbol, self.amount)

    def convert(self, other):
        """ Convert other amount to our currency """
        new_amount = ((other.amount / self.currency_rates[other.symbol]) * self.currency_rates[self.symbol])
        return Money(self.symbol, new_amount)

    def __add__(self, other):
        new_amount = self.amount+self.convert(other).amount
        return Money(self.symbol,new_amount)


class Server:
    services = [
        {'active': 'false', 'protocol': 'ftp', 'port': 21},
        {'active': 'true', 'protocol': 'ssh', 'port': 22},
        {'active': 'true', 'protocol': 'http', 'port': 80},
    ]


# 迭代器
class IterableServer:
    def __init__(self):
        self.current_pos = 0  # 初始化位置为0

    def __iter__(self):  # 实现了__next__ 可以直接返回self
        return self

    def __next__(self):
        while self.current_pos < len(self.services):
            service = self.services[self.current_pos]
            self.current_pos += 1
            if service['active']:
                return service['protocol'], service['port']
        raise StopIteration


mny = Money('$', 5.5)
mnx = Money('€', 6.5)
mnr = Money('¥', 100)
print(mny + mnx + mnr)
