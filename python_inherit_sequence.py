#author_by zhuxiaoliang
#2018-07-06 上午11:10

#多线程继承顺序
'''
新式类和经典类区别
1、python2.2版本后出现了新式类，新式类是是指继承某个类的类，比如：
class A：
    pass
这里A默认继承了（object）
也可以显示继承object。
老式类指的是在类树中未继承任何类。
2、python3以后不区分新旧类，均为新式类。
3、多继承顺序区别：
新式类是多继承中采用c3算法，类广度优先，不是真正的广度优先
就是类采用深度优先算法。

'''
"""
多继承示例
"""
class A(object):
    def say(self):
        print('A hello:',self)

class B(A):
    def eat(self):
        print('B eating:',self)

class C(A):
    def eat(self):
        print('C eating:',self)


class D(B,C):
    def say(self):
        super().say()
        print('D hello:',self)
    def dinner(self):
        self.eat()

d = D()
print(d.eat())
#D的继承遍历图 MRO 方法解析顺序
print(D.mro())
print(D.__mro__)