def countdown(n):
    if n <= 0:
        print 'finish!'
    else:
        print n
        countdown(n-1)
n=int(input("enter a num"))
print countdown(n)
