
print('your total amount is')
totalbalance=int(input('enter the total balance'))
print('this is your total amount')
# totalbalance='70000'
a='on'
b='exit'

c=input("enter the option \n")
# print(c)
if c=='on':
    print('welcome to atm')
    print("##### $$$$$ #####")
    print('how cxan we help u')
    d='deposit'
    e='withdraw'
    f='check my balance'
    g=input("enter the option \n")
    if g=='d':
        print(" how much money u want to deposit")
        money=int(input("enter the amount \n"))
        print('wait fo few seconds')
        if money<10000:
            print("the amount is deposited")
        else:
            print('too much money cant be deposited')
    
        
    elif g=='e':
            print('how much money u want to with draw from atm')
            rupee=int(input('entert eh amount'))
            if rupee<10000:
                print("the transaction is done")
            
                n=input("enter the option")
                if n== 'check':
                    print(totalbalance-rupee)
                else:
                    print(" i will see next time")
            
                # print(" the transcation is failed")    
            else:
                print("the transscation is not sucessful")

    # elif g=='f':
    #     print('checking the balance')
    #     # i=input('entert the option')
    #     if n == 'check':
    #         print(totalbalance-rupee)

        
            
    else:
            pass

    # else:
        # pass
else:
    print('visit again')

