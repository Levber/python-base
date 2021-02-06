'''
一.dict 字典，无顺序要求，即内部存放的顺序与key放入的顺序没有关系，以键值对存储值，具有极快的查找速度，用冒号：组成键值对，多次对一个key放入value，后面的值会把前面的值冲掉,要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
删除一个key时，用pop
和list比较，dict有以下几个特点：

1.查找和插入的速度极快，不会随着key的增加而变慢；
2.需要占用大量的内存，内存浪费多。
而list相反：

1.查找和插入的时间随着元素的增加而增加；
2.占用空间小，浪费内存很少。
所以dict是利用空间来换取时间的一种方法
在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

二、set和dict类似，也是一组key的集合，但不存储value，由于key不能重复，所以在set中没有重复的key，set中也不能包含可变对象，
'''

d = {'张三': 89, '李四': 79, '王麻子': 98, }
print(d['张三'])
'Thomas' in d  # 通过in 判断key是否存在
d.get('Thomas')  # 通过get方法判断，如果不存在则返回none
d.get('Thomas', 77)  # 如果不存在，可指向自己指定的值
print(d.get('Thomas', 77))
print('pop(key)方法，删除对应的键值对')
print(d.pop('王麻子'))  # 删除王麻子的分值
print(d)
print('需要特别注意的是：dict的key必须是不可变对象')
print('- -' * 50)
s = set([1, 2, 3, 4])
print(s)
print('通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果')
s.add(6)
s.add(6)
s.add(6)
print(s)
print('remove(key)方法可以删除元素')
s.remove(1)
print(s)
print('set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作')
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = s1 & s2  # 交集
print(s3)
s4 = s1 | s2  # 并集
print(s4)
s5 = ([1, 2, ['A', 'B']])  # list在集合中和在dict中一样，list本身是可以改变的
print(s5)
s5[2][0] = 'a'
print(s5)

x = ['b', 'c', 'a']
x.sort()  # ;list可变，sort方法排序
print(x)
a = 'abc'
b = a.replace('a', 'A')  # replace方法是作用在字符串上‘abc’上的，而不是变量a，这里就相当于直接改变了内容abc，重新创建了一组字符串，赋值给变量b，所以打印a的时候，还是abc，打印b的话就是Abc
print(b)
print(a)
print('所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的')
