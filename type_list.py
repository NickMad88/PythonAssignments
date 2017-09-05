testlist= ['hey',1,2,6]
sum = 0
newstring = ""
intcounter = 0
strcounter = 0
for item in testlist:
    if type(item) is int:
        sum += item
        intcounter += 1
    elif type(item) is str:
        newstring += item
        strcounter += 1

if intcounter > 0 and strcounter == 0:
    print "The list you entered is of integer type"
elif intcounter == 0 and strcounter > 0:
    print "The list you entered is of string type"
else:
    print "The list you entered is of mixed type"
        
print newstring
print sum