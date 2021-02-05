'''
list和tuple（列表和元组）
一、list [] 一种有序，可变的集合，列表里面的元素可以是不同的数据类型，也可以嵌套列表（也可以叫做二维数组）,list如果没有元素，则长度len（list）为0
二、元组tuple （） 元组是一种有序，初始化后不可修改的集合
'''
classmates = ['张三', '李四', '王五', '赵六', '阿三']
print(classmates)
print(len(classmates))
print(classmates[2])  # 用索引访问，超出索引范围时，报错IndexError
classmates.insert(1, 'jack')  # 指定下标插入元素用insert（）方法
print(classmates)
classmates.append('王麻子')
print(classmates)
print('删除列表 “末尾” 的元素用pop()方法,也可以用索引的方式pop（1）删除')
class2 = classmates.pop()
print(class2)
print(classmates)
classmates.pop(1)
print(classmates)
classmates[1] = '李老四'  # 根据下标修改对应的元素值
print(classmates)
L = ['Apple', 123, True]  # 列表里面的元素可以是不同的数据类型
print(L)
B = ['hello', 123, False, ['123', 'lisa'], '尼桑']  # 列表嵌套（二维数组）
print(B)
print(B[3][1])
print('- -' * 50)
print('tuple 元组不可变')
t = (1, 2)  # 元组不可变，所以没有append，insert等方法
print(t)
t1 = ()  # 定义一个空元组
print(t1)
t2 = (1,)  # 如果元组中只有一个元素，则需要用逗号
print('tuple的指向永远不变，比如‘a’不可变为‘B’，但里面的list本身是可以改变的')
t3 = ('a', 'b', ['A', 'B'])
t3[2][0] = 'X'
t3[2][1] = 'Y'
print(t3)
