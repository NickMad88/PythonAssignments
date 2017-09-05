# Multiples - Part I - Print all odds from 1-1000
for i in range(1, 1000, 2):
    print i

#Multiples - Part II - Prints all multiples of 5 from 5 to 1,000,000
for i in range(5, 1000000):
    if i % 5 == 0:
        print i

# Sum List - Prints the sum of all values in the list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

#Average List - Prints the aerage of the values in the list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
avg = sum / len(a)
print avg