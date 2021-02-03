# 廖雪峰教程
# 字符串
print(ord('A'))
print(ord('中'))
print(chr(25991))
# 二进制表示字符串
print('\u4e2d\u6587')   # 得出结果：中文
print('使用encode（）方法可以编码为指定的bytes字节')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print('使用decode（）方法将字节流转换成字符串')
print(b'ABC'.decode('ascii'))
print('中'.encode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))     # errors='ignore' 可以忽略错误的字节
print(len('中文'))
print(len('ABC'))
print(len('中文'.encode('utf-8')))
print(len('ABC'.encode('ascii')))
# 格式化  %s表示用字符串替换，%d表示用整数替换，%f  浮点数 ，%x  十六进制整数
print('hell,%s'%'world')
print('%.2f' % 3.1415926)   # 保留两位小数的浮点数
