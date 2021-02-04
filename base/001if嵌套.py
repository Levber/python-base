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
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print("玩家获胜！！")
elif player == computer:
    print("平局！！")
else:
    print("电脑获胜！！！")
