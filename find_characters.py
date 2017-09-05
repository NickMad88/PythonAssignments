word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

for item in word_list:
    for letters in item:
        print item
        if letters == char:
            new_list.append(item)

print new_list
