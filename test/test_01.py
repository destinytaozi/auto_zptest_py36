# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_demo
   Description :
   Author :       Destiny
   date：          2018/8/24 14:50
-------------------------------------------------
   Change Activity:
                   2018/8/24 14:50
-------------------------------------------------
"""
__author__ = 'Destiny'

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

s = Server()
for protocol, port in s:
    print('service %s is running on port %d'%(protocol,port))

# class InterableServer:
#
#     def __init__(self):
#         self.current_pos = 0
#         self.services = Server.services
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.current_pos < len(self.services):
#             service = self.services[self.current_pos]
#             self.current_pos+=1
#             if service['active']:
#                 return service['protocol'],service['port']
#         raise StopIteration
#     next = __next__

# InterableServer()
# for protocol,port in InterableServer():
#     print('service %s is running on port %d' % (protocol,port))