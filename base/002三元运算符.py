'''
三目运算符（三元运算符或者三元表达式）的作用：化简简单的if。。。else条件语句
语法：条件成立执行的表达式  if 条件  else 条件不成立执行的表达式
'''
a = 1
b = 2
c = a + 1 if a < b else b < a
print(c)
