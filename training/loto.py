import random

lst = []

while len(lst) < 7:
    if(len(lst) < 5):
        max = 50
    else:
        max = 12

    num = random.randint(1,max+1)
    if(num not in lst):
        lst.append(num)

print(lst)