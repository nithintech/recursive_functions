def sumlist(a):                #a= numberlist
   if len(a) == 1:
        return a[0]
   else:
        return a[0] + sumlist(a[1:])

print sumlist([2,3,6,7,1,5])
