'''
for循环遍历：
'''
classmates = ['张三', '阿三', '李四', '王麻子', '赵六']
for student in classmates:
    print(student)

sum = 0
for x in range(0, 100):
    sum = sum + x
print(sum)  # 在循环外打印就是最终的结果，如果在循环内打印就是每一次相加的结果

n = 1
while n < 100:
    if n > 10:  # 打印出10以内的每一个正整数
        break  # break跳出当前循环，结束
    print(n)
    n = n + 1
print('END')

x = 0
while x < 10:
    x = x + 1
    if x % 2 == 0:  # 打印10以内取余为0 的正整数
        continue  # continue 跳出循环继续执行
    print(x)
# 应用一：累加1-100求和：分析1+2+3+4+...+100、
i = 0
result = 0
while i <= 100:
    result = result + i
    i = i + 1
print(result)
