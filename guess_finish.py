from random import randint
num = randint(1,100)

print 'what do i think?'
bingo = False

while bingo == False:
    answer = input()
    if answer < num:
        print 'too small!'
    if answer > num:
        print 'too big!'
    if answer == num:
        print 'bingo'
        bingo = True