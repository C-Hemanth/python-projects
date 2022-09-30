# runs=1,2,3,4,6


# wicket=5
# wide=7
# nob=8tail

# catch=9

# import random
# b=random.randint(1,9)
# print(b)



import random
toss=random.randint(1,2)
tail='1'
head='2'
me=int(input("enter the toss"))
print(toss)
if toss==me:
    print('won')
else:
    print('lose')