'''
调用函数--------，要调用一个函数，就得先知道函数的名称和参数，比如绝对值的函数abs，只有一个参数,
定义函数--------，使用def语句定义函数，
                    定义函数时，需要确定函数名和参数个数；
                    如果有必要，可以先对参数的数据类型做检查；
                    函数体内部可以用return随时返回函数结果；
                    函数执行完毕也没有return语句时，自动return None。
                    函数可以同时返回多个值，但其实就是一个tuple。
函数的参数-------，
递归函数---------，在函数内部调用自己本身，这个函数就是递归函数
'''
print(abs(-100))
print('调用函数的时候，如果传入的参数数量或参数类型不对，会报TypeError的错误')
print(max(1, 2, 9, -10, 100, ))  # max函数可以接受任意多个参数,但参数类型不能错
# python中还包含了很多数据转换类型的函数，比如int（），float（），str()等
print(hex(255))  # hex()函数把一个整数转换成十六进制表示的字符串


def new_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(new_abs(-192))


# 空函数，pass作用就是相当于占位符，可以让代码运行起来
def nop():
    pass


# pass 也可与运行在其他的语句里面：
age = int(input("请输入你的年龄："))
if age > 18:
    pass  # 这里的pass就相当于占位符，临时让代码正常运行起来


# 参数检查：isinstance（）函数，通过规定只允许整数和浮点型的参数
def new_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(new_abs1(-11))

# 函数返回多个值
import math


def move(x, y, step, angle=0):  # angle 角度
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny  # 返回的只是一个tuple


print(move(100, 60, 100, angle=30))


# 练习
def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    else:
        return '无解'


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

"""
函数的参数-------
                位置参数
                默认参数，（存在默认的参数值）参数调用时，如果存在参数变化幅度很小，则考虑使用默认参数，大大降低函数调用的难度****默认参数一定要指向不变对象来实现，否则在多次调用时，会以上次的结果作为默认参数
                可变参数，定义一个可变参数，就是在参数前面加一个*号
                关键字参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
                命名关键字参数，对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
"""


# 位置参数
def power(x):  # x就相当于位置参数
    return x * x


print('x的平方：', power(10))


# x的n次方
def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power1(5, 5))


# 默认参数，
def power(x, n=2):  # n=2作为一个默认参数，可以减少函数调用的复杂度
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 3))


# 默认参数必须指向不变对象
def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2]))
print(add_end([2, 3]))
# L=[] 本身是可变对象，多次调用时，后面的函数就会以前面的结果作为默认参数
print(add_end())
print(add_end())
print(add_end())


# 给默认参数定义一个不可变对象None
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())  # 无论调用多少次，都只会传入一个默认参数END
print(add_end())
print(add_end())

# 可变参数 *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print('可变参数')


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc())


# 关键字参数
def person(name, age, **kw):
    print('name：', name, 'age:', age, 'other:', kw)  # 没有return 的解析式时，会返回一个none


print(person('Jack', 28))
print(person('Tom', 20, gender='boy', city='chongqing'))


# 不受限制的传入关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name：', name, 'age:', age, 'other:', kw)


print(person('Tonney', 20, job='test', city='chongqing', id=1021))


# 限制参数的名字，命名关键字参数需要一个特殊的分隔符，* ，* 号后面的参数被视为命名关键字参数
def person(name, age, *, job, city):
    print(name, age, job, city)


print(person('Jhon', 15, job='test', city='changshou'))


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, job, city):
    print(name, age, args, job, city)


print(person('Jhon', 15, 'ID:', 21, job='test', city='changshou'))

"""
递归函数：函数内部调用自己的函数，
尾递归可以解决栈溢出；
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))
