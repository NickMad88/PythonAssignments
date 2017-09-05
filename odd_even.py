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