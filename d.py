import re
import random

def dice_bot(msg, rep):
    pattern = re.compile('\d+d\d+', re.I)
    m = pattern.match(msg)
    if not m == None:
        rep = None
        dice = m.group(0)
        rep = dice_bot_random(dice, rep)
        print('dice_bot：result：', m)
        print('dice_bot：list：', rep)
        print('dice_bot：total：', sum(rep))
    else:
        rep = None
    return rep

def dice_bot_random(dice, rep):
    rep = []
    print('dice_bot_random：' ,dice)
    d = dice.split('d')
    print('dice_bot_ramdom_num:', d[0])
    print('dice_bot_ramdom_max:', d[1])
    dice_bot_ramdom_num = int(d[0])
    while dice_bot_ramdom_num > 0:
        dice_bot_ramdom_num = dice_bot_ramdom_num - 1
        r = random.randint(1,int(d[1]))
        rep.append(r)
    return rep

rep = None
while True:
    msg = input('MSG:')
    if msg == 'q':
        break
    else:
        rep = dice_bot(msg, rep)
        print('main：', rep)
