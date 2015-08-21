def digitsum(num):
       if num == 0:
           return 0
       else:
           return ((num%10) +(digitsum(num/10)))

num = int(raw_input("enter a number\n"))
print "sum of digit is",digitsum(num)
