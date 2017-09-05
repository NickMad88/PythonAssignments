import random
from random import randint

def tenscores():
    counter = 0
    while counter < 10:
        random_num = random.randint(60, 100)
        score = random_num
        print score
        if random_num >= 90:
            print "Your grade is A"
        elif random_num >= 80:
            print "Your grade is B"
        elif random_num >= 70:
            print "Your grade is C"
        elif random_num >= 60:
            print "Your grade is D"
        
        counter += 1
print tenscores()