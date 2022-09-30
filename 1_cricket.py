print('welcome to the official cricket game')

Team_A=('INDIA','ENGLAND','AUSTRALIA','NEW ZEALAND','SOUTH AFRICA','WEST INDIES','PAKISTAN','AFGANISTAN','BANGLADESH','SRI LANKA','IRELAND','ZIMBAMBAE','NETHERLANDS')
Team_B=('INDIA','ENGLAND','AUSTRALIA','NEW ZEALAND','SOUTH AFRICA','WEST INDIES','PAKISTAN','AFGANISTAN','BANGLADESH','SRI LANKA','IRELAND','ZIMBAMBAE','NETHERLANDS')

player1=input('enter your team A : ' )
player2=input('enter your team B : ' )

tail=1
head=2
bat=3
bowl=4

if player1!=player2 :
    print("starting your match")

    import random
    toss=random.randint(1,2)
    # def game(comp,me):

    me=int(input('choose your option'))
    print(toss)

    if me==toss:
            print('you have won the toss')
            # if 'you have won the toss':
            #     print(' you select bat/bowl')
            # elif 'comp have won the toss':
            #     print('comp select bat/bowl')
            # else:
            #     pass
    elif me!=toss:
        print("comp have won the toss")
    else:
        pass

    
          
    if 'you have won the toss':
                dec=input('enter bat/bowl')
                if dec=='bat':
                    print('you hav chosen to bat')
                else:
                    print('you hav chosen to bowl')
    # else:
                # pass
    elif 'comp have won the toss':
        import random
        deci=random.randint(3,4)
        print(deci)
        if deci==3:
                    print('comp hav chosen to bat')
        else:
                    print('comp chos eot bowl')
    else:
                pass
            # def game(comp,me):
            #     pass
elif player1==player2 :
    print("choose a different opponent")
else:
    pass

