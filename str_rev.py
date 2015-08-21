def reverse(strng):
    if strng == "":
        return strng
    else:
        return reverse(strng[1:]) + strng[0]

strng = str(raw_input("enter a string\n"))
print "reverse of string\n",reverse(strng)
