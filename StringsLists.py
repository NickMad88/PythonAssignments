# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.replace("day", "month", 1)


#Min and Max
x =[2,54,-2,7,12,98]
print max(x)
print min(x)

#First and Last
firstandlast = ["hello",2,54,-2,7,12,98,"world"]
first = firstandlast[0]
last = len(firstandlast)-1
print first + firstandlast[last]

#New List
y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()
list1 = y[:len(y)/2]
list2 = y[(len(y))/2 - 1:]
list2[0] = list1
print list2
