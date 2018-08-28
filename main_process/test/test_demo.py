#coding = utf-8
#This file named test_01.py
#his duty is to test some program.
class Server:
    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]
    def __iter__(self):
        for service in self.services:
            if service['active']:
                yield service['protocol'],service['port']

class InterableServer:

    def __init__(self):
        self.current_pos = 0
        self.services = Server.services

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_pos < len(self.services):
            service = self.services[self.current_pos]
            self.current_pos+=1
            if service['active']:
                return service['protocol'],service['port']
        raise StopIteration
    next = __next__

InterableServer()
for protocol,port in InterableServer():
    print('service %s is running on port %d' % (protocol,port))

# class Money:
#     currency_rates = {
#         '$':1.0,
#         '£':0.7739,
#         '€':0.88,
#         '¥':6.8395,
#     }
#
#     def __init__(self,symbol,amount):
#         self.symbol = symbol
#         self.amount = amount
#
#     def __repr__(self):
#         print('%s%.2f'%(self.symbol,self.amount))
#         return '%s%.2f'%(self.symbol,self.amount)
#
#     def __str__(self):
#         return '%s%.2f'%(self.symbol,self.amount)
#
#     def convert(self,other):
#         new_amount = (other.amount/self.currency_rates[other.symbol]*self.currency_rates[self.symbol])
#         return Money(self.symbol,new_amount)
#
#     def __add__(self, other):
#         new_amount = self.amount+self.convert(other).amount
#         return Money(self.symbol,new_amount)
#
#     def transfor2Doll(self):
#         new_amount = self.amount / self.currency_rates[self.symbol]
#         return Money('$',new_amount)
#
# m1=Money('£',20)
# m2=Money('¥',50)
# m_sum=m1+m2
# m_dollor=m_sum.transfor2Doll()
# print(m_sum)
# print(m_dollor)
