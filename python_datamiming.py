#author_by zhuxiaoliang
#2018-07-05 下午12:44

import  requests
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = requests.get(url)

localFile = open('iris.csv', 'wb+')
localFile.write(u.content)
localFile.close()

from numpy import genfromtxt,zeros

data = genfromtxt('iris.csv',delimiter=',',usecols=(0,1,2,3))
target = genfromtxt('iris.csv',delimiter=',',usecols=(4),dtype=str)

#print(data.shape)
#print(target.shape)
#print(target)
"""
(150, 4)
(150,)

"""

from pylab import plot,show


'''
绘图
plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
plot(data[target=='virginica',0],data[target=='virginica',2],'go')
show()'''
#将字符串转换成整形数据
t = zeros(len(target))
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3

print(t.shape)
'''[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
 1. 1. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.
 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2. 2.
 2. 2. 2. 2. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3.
 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3. 3.
 3. 3. 3. 3. 3. 3.]


'''

#高斯贝叶斯分类器
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(data,t) # training on the iris dataset