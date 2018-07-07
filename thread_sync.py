#author_by zhuxiaoliang
#2018-07-05 下午3:39

"""
　　A. Semaphore（信号量）

　　在多线程编程中，为了防止不同的线程同时对一个公用的资源（比如全部变量）进行修改，需要进行同时访问的数量（通常是1）的限制。信号量同步基于内部计数器，每调用一次acquire()，计数器减1；每调用一次release()，计数器加1.当计数器为0时，acquire()调用被阻塞。

"""
import time
from random import random
from  threading import Thread,Semaphore,enumerate
sema = Semaphore(3)

def foo(tid):
    with sema:
        print()
