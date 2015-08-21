def binary(num):
   if num > 1:
       binary(num/2)
   print str(num % 2) + ''

dec = int(input("Enter an integer: "))
binary(dec)
