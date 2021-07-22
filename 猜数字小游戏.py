import random
guess = random.randint(0,100)
change = 10
print(''
      '           游戏规则'
      '           你有10次机会猜出一个数字'
      '           这个数字的范围在0——100之间'
      '           每猜错一次都会提示一次')
while True:
    try :
        num = int(input('请输入一个数字：'))
        if change == 1:
            print('次数已用完,本轮的数字是{}'.format(guess))
            break
        else:
            change -= 1
            a = 10 - change
            if num > guess:
                print('这个有点大,你还有{}次机会'.format(change))
            elif guess == num:
                print('恭喜你答对了,仅用了{}次就猜出来了。'.format(a))
                break
            else:
                print('这个数有点小,你还有{}次机会'.format(change))
    except:
        print('请输入数字')
        break
print('游戏结束')

# maker : Wen Kaijin
#date   : 7/22/2021
#versiom : 1.0