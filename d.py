#將可接受*d*的指令
#d前面的是骰幾次
#d後面的是骰子面數
#例:2d10，骰兩次十面骰子


import re #載入正則
import random #載入random

def dice_bot(msg, reps):#這裡是判斷輸入的內容是不是指令的範圍
    pattern = re.compile('\d+d\d+', re.I)#設定正則規則，re.I將可無視大小寫
    m = pattern.match(msg) #判斷輸入的是不是指令
    if not m == None: #如果m存在
        rep = None
        dice = m.group(0) #將正則找到的指令設置為dice
        rep = dice_bot_random(dice, rep) #開始擲骰程序
        print('dice_bot：result：', m)
        print('dice_bot：list：', rep)
        print('dice_bot：total：', sum(rep))
        reps = rep, sum(rep) #把結果清單跟結果總和放在一起
    else: #如果他不存在
        reps = None
    return reps

def dice_bot_random(dice, rep): #這裡是進行指令解析與骰子的地方
    rep = []
    dice = dice.replace('D','d') #如果使用者輸入的D是大寫，將它轉換成小寫
    print('dice_bot_random：' ,dice)
    d = dice.split('d') #將dice分割成前後兩個數值
    print('dice_bot_ramdom_num:', d[0]) #骰幾次
    print('dice_bot_ramdom_max:', d[1]) #骰幾面的骰子
    dice_bot_ramdom_num = int(d[0]) #將骰幾次變成數值
    while dice_bot_ramdom_num > 0: #骰子的數字歸零之前會一直骰
        dice_bot_ramdom_num = dice_bot_ramdom_num - 1
        r = random.randint(1,int(d[1])) #骰
        rep.append(r) #將骰子結果存入rep
    return rep #回傳rep

reps = None
while True:
    msg_all = []
    message = input('MSG:') #讓使用者輸入指令
    msg_all = message.split(' ',1) #將指令分割成指令區域與非指令區域
    msg = msg_all[0] #將指令區域設定成msg
    if msg == 'q': #如果輸入q，程式就會結束
        break
    else:
        if len(msg_all) == 1: #如果沒有註解的話，就只會輸出骰子結果
            reps = dice_bot(msg, reps)
            print('main：', reps)
        else: #如果有註解的話，會把註解放在結果後面
            reps = dice_bot(msg, reps)
            print('main：', reps, msg_all[1])
