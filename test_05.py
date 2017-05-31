print "what do you think I am?"
name = raw_input()
print "oh yes I am "
print name
num = 10
print "guess what i think?"
answer = raw_input()

res = answer < num
print 'too small?'
print res

res = answer > num
print "too big?"
print res

res = answer == num
print "equal?"
print res
