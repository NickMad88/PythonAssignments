# Integer - If greater than or equal to 100, "big number!", else "small number!"
integertest = 455
if integertest >= 100:
    print "That's a big number!"
elif integertest < 100:
    print "That's a small number!"

String - if string >= 50 characters, print "Long Sentence", else "Short Sentence"
stringtest = "ell me and I forget. Teach me and I remember. Involve me and I learn."
if len(stringtest) >= 50:
    print "Long Sentence!"
elif len(stringtest) < 50:
    print "Short Sentence!"

# List - length of list is greater than or equal to 10, print "Big List!", else "Short list!"
listtest =[4,34,22,68,9,13,3,5,7,9,2,12,45,923]
if len(listtest) >= 10:
    print "Long List!"
elif len(listtest) < 10:
    print "Short List!"