import random
list = []
string = "Hello, world!"

for i in string:
    list.append(i)

random.shuffle(list)

string = ''.join(list)

print(string)