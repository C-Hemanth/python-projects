score=0
while score<1000:
    i=0
    while i<30:
        import random
        comp=random.randint(1,10)
        player=int(input("enter the num \n"))
        if comp != player:
            if player>10:
                print('you have entered wrong number')
            else:
                print(comp)
        
            print("total score is",player)
            score=score+player
            print("the total score is ",score)
            i=i+1
            print("the total balls face dis",i)
        else:
            print(comp)
            print('the total score is ',score)
            # print("the total balls faced is",i)
            if comp == player:
                print("the total balls faced is ",i+1)
            else:
                pass
    break;