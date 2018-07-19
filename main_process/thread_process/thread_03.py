# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       thread_demo
    Description:
    Author:          destiny
    date:            2018/7/16 21:18
--------------------------------------------------------------------
    Change Activity:
                    2018/7/16 21:18
--------------------------------------------------------------------
"""
__author__ = 'destiny'

import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self) #重写treading内部初始化
        self.threadID = threadID    #线程id
        self.name = name     #线程名字
        self.q = q          #线程传递参数
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)     #线程调用主函数
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")