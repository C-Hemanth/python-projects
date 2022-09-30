import random
gold=random.randint(100000,1000000)
exiler=random.randint(100000,1000000)
lootedgold=random.randint(0,gold)
lootedexiler=random.randint(0,exiler)
# gainedgold=looted<gold
# gainedexiler=looted<exiler
# gaingold=
d=random.randint(1,2)
# print(d)
print(gold)
print(exiler)
a=input("enter the option")
if a=='attck':
    print('attcking started')
    print(f"the gold gained after attcking us {lootedgold}")
    print(f"the exiler gained after attcking us {lootedexiler}")
    if d==1:
        print('victory')
    elif d==2:
        print('defeat')
    else:
        pass
else:
    print("returning back")