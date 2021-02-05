'''
猜拳游戏案例
1.出拳
    电脑：固定 1，剪刀；随机2
2.判断输赢
    1.玩家获胜
    2.平局
    3.电脑获胜
'''
# 电脑随机出拳
import random

player = int(input("请输入数字代表出拳：0-石头，1-剪刀，2-布"))
computer = random.randint(0, 2)
print(computer)
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or (
        (player == 2) and (computer == 0)):  # 分析玩家获胜的情况有哪些
    print("玩家获胜！！")
elif player == computer:
    print("平局！！")
else:
    print("电脑获胜！！！")

age = int(input('请输入你的年龄：'))
if age >= 18:
    print('your age is', age)
    print('you are adult!!')
else:
    print('your age is', age)
    print('teenager')
'''
身体质量指数bmi=体重/身高的平方
1.体重过轻：bmi<18.5
2.正常值范围：18.5≤bmi<24
3.偏重：bmi≥24
'''
h = float(input("请输入你的身高："))
w = float(input("请输入你的体重："))
bmi = w / (h ** 2)
if bmi < 18.5:
    print('你的体重有点轻！！', bmi)
elif bmi >= 24.0:
    print('你的体重有点重了！！！', bmi)
elif bmi < 24.0 and bmi >= 18.5:
    print('你的体重身体指标非常正常', bmi)
