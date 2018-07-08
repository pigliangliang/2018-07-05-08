#author_by zhuxiaoliang
#2018-07-06 上午11:43

'''
python 异步编程：协程与异步IO
GIL锁：
对于计算密集型的使用多进程，对于IO密集型的使用多线程，在IO阻塞时候让出gil锁。

'''
#yiel实现生成器
def coroutine():
    reply = yield 'hi'
    yield reply

c = coroutine()
#print(c.__next__())
#print(c.send('pig'))
#输出：
#hi
#pig

from  collections import deque
def student(name,homeworks):
    for homework in  homeworks.items():
        yield (name,homework[0],homework[1])

#class Teacher(object):
    def __init__(self,students):
        self.students = deque(students)
    def handle(self):
        while (len(self.students)):
            student = self.students.pop()

            try:
                homework = next(student)
                print('handling',homework[0],homework[1],homework[2])
            except StopIteration:
                pass
            else:
                self.students.appendleft(student)


#Teacher([
    student('Student1', {'math': '1+1=2', 'cs': 'operating system'}),
    student('Student2', {'math': '2+2=4', 'cs': 'computer graphics'}),
    student('Student3', {'math': '3+3=5', 'cs': 'compiler construction'})
#]).handle()

'''
斐波那一数列
def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b,end=" ")#控制输出 1 1 2 3 5 8 
        a, b = b, a + b
        n = n + 1
fab1(6)
'''
#使用yield生成器
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n+=1
f = fib(5)
#print(f)  <generator object fib at 0x103fec410>
# yield from iterable 本质是 for item in iterable yield item
#for 输出

#for i in f:
#   print(i,end=' ') #1 1 2 3 5


# yield from 代替for’
'''
l = [1,2,3]
def vgg(l):
    yield  from l#此处只要是个生成器就可以
for i in vgg(l):
    print(i,end= ' ')#输出同上

#包含多个yield from
def g(x):
    yield from range(x, 0, -1)
    yield from range(x)
#print(list(g(5)))
for g  in g(5):
    print(g,end= ' ')

#按序输出 5 4 3 2 1 0 1 2 3 4


#利用yield from 语句向生成器发送数据
import time
def consumer_work(len):
    print("writer:")
    v = 1
    while True:
        w = yield  v
        print('consumer %s',w)
        v*=len
        time.sleep(0.1)

def consumer(coro):
    yield  from coro

def produce(c):
    c.send(None)
    for i in range(1,5):
        print('produce %s' ,i)
        j = c.send(i)
        print('receive %s',j)

    c.close()
c1 = consumer_work(10)
c2 = consumer(c1)
produce(c2)
输出
writer:
produce %s 1
consumer %s 1
receive %s 10
produce %s 2
consumer %s 2
receive %s 100
produce %s 3
consumer %s 3
receive %s 1000
produce %s 4
consumer %s 4
receive %s 10000

解释：yield from 从yield中拿数据。
j = c.send(i)中，j的值是yield 值，即v；
send发送的值i是yield语句的值，即w值


#回到asynnio模块
import  asyncio
import datetime
@asyncio.coroutine
def display_date(num,loop):
    end_time =loop.time()+10.0
    while True:
        print('Loop:{} time: {}'.format(num,datetime.datetime.now()))
        if loop.time()+1.0>=end_time:
            break
        yield from asyncio.sleep(2)


loop = asyncio.get_event_loop()  # 获取一个event_loop
tasks = [display_date(1, loop), display_date(2, loop)]
loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
loop.close()

Loop:2 time: 2018-07-08 11:28:38.916692
Loop:1 time: 2018-07-08 11:28:38.916768
Loop:2 time: 2018-07-08 11:28:40.921490
Loop:1 time: 2018-07-08 11:28:40.921617
Loop:2 time: 2018-07-08 11:28:42.924768
Loop:1 time: 2018-07-08 11:28:42.924900
Loop:2 time: 2018-07-08 11:28:44.929780
Loop:1 time: 2018-07-08 11:28:44.929908
Loop:2 time: 2018-07-08 11:28:46.935182
Loop:1 time: 2018-07-08 11:28:46.935312
Loop:2 time: 2018-07-08 11:28:48.937996
Loop:1 time: 2018-07-08 11:28:48.938177

'''
#python 3.5 引入了async/await关键字，上面的代码我们可以这样改写，使用async代替了@asyncio.coroutine，使用了await代替了yield from，
import asyncio
import datetime
async def display_date(num, loop):  # 声明一个协程
    end_time = loop.time() + 10.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(2)  # 等同于yield from
loop = asyncio.get_event_loop()  # 获取一个event_loop
tasks = [display_date(1, loop), display_date(2, loop)]
loop.run_until_complete(asyncio.gather(*tasks))  # "阻塞"直到所有的tasks完成
loop.close()









