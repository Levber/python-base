# 廖雪峰教程
# 字符串
print(ord('A'))  # ord（）函数获取对应字符串的数字编码
print(ord('中'))
print(chr(25991))  # chr()函数把编码转换为对应的字符
print('= =' * 20)
# 二进制表示字符串
print('\u4e2d\u6587')  # 打印二进制编码，得出结果：中文
print('使用encode（）方法可以打印出指定编码类型的bytes字节')
print('ABC'.encode('ascii'))  # 英文字符的byte字节是其本身
print('中文'.encode('utf-8'))
print('使用decode（）方法将字节流转换成字符串')
print(b'ABC'.decode('ascii'))
print('中'.encode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))  # errors='ignore' 可以忽略错误的字节
print(len('中文'))
print(len('ABC'))
print(len('中文'.encode('utf-8')))
print(len('ABC'.encode('ascii')))
print('= =' * 20)
# 格式化  %s表示用字符串替换，%d表示用整数替换，%f  浮点数 ，%x  十六进制整数
print('hell,%s' % 'world')
print('%.2f' % 3.1415926)  # 保留两位小数的浮点数
print('%2d-%02d' % (3, 1))  # 补0和占位空格数
print('hello,{0},成绩提升了{1:.2f}%'.format('小明', 17.125))  # format()方法是依次替换字符串内的占位符
print('-' * 50)
a = 'boy'
b = 12
print(f'小明是一个善良的{a},今年已经{b}岁了！！')  # f-string 格式化字符串，变量替换
