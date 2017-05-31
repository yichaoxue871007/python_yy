from random import choice

score_you = 0
score_com = 0
direction = ['left','center','right']

for i in range(5):
    print '==== round%d - You Kick ====' %(i+1)
    print 'choose one side to shoot!'
    print 'left,right,center'
    you = raw_input()
    print 'You kicked' + you
    com = choice(direction)
    print 'computer saved' + com
    if you != com:
        print 'Goal!'
        score_you +=1
    else:
        print 'oops'
    print 'score:%d(you) - %d(com)\n' %(score_you,score_com)