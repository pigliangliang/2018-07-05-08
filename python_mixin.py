#author_by zhuxiaoliang
#2018-07-05 下午11:14

#python mixin
'''
mixin 是一种类，这种类包含了其他类所要使用的方法，比如某个类需要的某种行为，允许程序员将一些代码注入到其他类中。mixin类扮演父类的角色，包含其他类
想要的功能，一个子类可以继承或者简单的重用该类。但是mixin类不必作为其他类的父类。
minxin鼓励代码重用。
优势：
1、允许许多类使用通用的功能，为多继承提供了一种机制，但是没有多成继承的复杂语义。
2、代码可重用
3、mixin允许使用和继承父类所需的功能，不一定是父类所有的功能。

py应用：
python中socketserver模块具有udpserver和tcpserver，分别作为udp和tcp套接字服务器的服务器。还有两个mixin类，ForkingMimin 和 ThreadingMixin

'''
from  socketserver import ThreadingMixIn,TCPServer
class ThreadingTCPServer(ThreadingMixIn,TCPServer):
    pass

#例如：定义两个迷信类
class AMixin(object):
    def fa(self,*args,**kwargs):
        return 'a'
class BMinxin(object):
    def fb(self,*args,**kwargs):
        return 'b'


class C (object):
    def fc(self,*args):
        return args[0]
"""
AMixin,BMixin 为D类提供接口数据，本质上并不是继承关系。
"""
class D(C,AMixin,BMinxin):
    def fd(self,*args,**kwargs):
        a = self.fa(*args,**kwargs)
        b = self.fb(*args,**kwargs)
        e = super().fc('e')
        return (a,b,e)

d = D()
print(d.fd())