
# Odd_Even - create function that counts form 1 to 2000, as loop runs, have number printed and declared of whehter it is odd or even
def odd_even():
    num = 1
    numberis = "Number is: "
    while num <= 2000:
        print numberis + str(num)
        if num % 2 == 0:
            print "This is an even number"
        else:
            print "This is an odd number"
        num += 1

print odd_even()

# Multiply - create function that iterates through each value in a list (eg a=[2,4,10,15] and returns a list where each value has been multiplied by 5)
list1 = [3,4,5,3]
def multiply(a,b):
    for item in range(len(a)):
        a[item] *= b
    return a
print multiply(list1, 5)