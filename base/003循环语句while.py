'''
1.语法
while 条件：
    条件成立执行代码块1
    条件成立执行代码块2
    ........
2.循环流程：循环体条件不成立时就跳出循环体
'''
i = 0
while i < 5:
    i += 1
    print(f"{i}你很重要吗")

# 应用一：累加1-100求和：分析1+2+3+4+...+100、
i = 1
result = 0
while i <= 100:
    result += i
    i += 1
print(result)
# 应用二：计算1-100的偶数和：分析：2+3+6+...+100;达成条件:1.和2取余数为0,2.直接偶数相加
i = 1
result = 0
while i <= 100:
    i += 1
    if i % 2 == 0:
        result += i
print(result)
# 计数器控制，让偶数累加
while i <= 100:
    i += 2
    result += i
print(result)
# while嵌套循环语句
j = 1
while j <= 3:
    i = 1
    while i <= 3:
        print(f"跑步{i}圈！！！")
        i += 1
    print(f"跑步完了再慢走{j}圈")
    j += 1
# continue 和 break 循环应用 ，continue是跳出当前循环继续执行，break是跳出当前循环不在继续执行
# 5个苹果，吃苹果，吃了3个就不吃了
# break
i = 1
while i <= 5:
    if i == 3:
        print(f"我吃了{i}个了，吃不下了！")
        break
    print(f"我吃了{i}个苹果！！！")
    i += 1
# continue
i = 1
while i <= 5:
    if i == 3:
        print(f"吃到了一个坏的，这个不吃了！")
        # 如果使用了continue，则要在之前改变计数器的值-----**************
        i += 1
        continue
    print(f"吃了{i}个苹果！")
    i += 1
# 打印*，一行5个，打印5行
a = 0
while a < 5:
    b = 0
    while b < 5:
        print("*", end='')
        b += 1
        # 打印一行
    print()
    a += 1
# 99乘法表
'''
1.打印一个表达式 x  *  x  = x*x
2一行打印多个表达式，，一行表达式的个数和行号数相等，--循环，一个表达式  不换行
3.打印多行表达式，--循环--一行表达式   换行
****注意：一行表达式的个数和行号数相等
'''
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f"{i}  *  {j}  = {i * j}", end="\t")
        i += 1
    print()
    j += 1
