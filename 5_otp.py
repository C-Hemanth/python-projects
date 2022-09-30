import random
randnum=random.randint(999,10000)
h=randnum
phonenum=(input("enter the number \n"))
generate='a'
b="your otp is generated it will be valid for 20 seconds"
enter='user have entered'
notenter='user have not entered'
# user=input("enter to generate \n")


if(len(phonenum)<11):
    print('click to generate otp')
    user=input("enter the option \n")
    if user=='generate':
        # print("your otp is generated it will be valid for 20 seconds")
        print(b)
        # print(f"your otp is {randnum}")
        print(f"your otp is '{h}' ")
        userr=input("enter the option \n")
        if userr == 'enter':
            print('please enter ur otp')
            userotp=int(input("enter the received otp \n"))
            if userotp==h:
                print("it is correct")
            else:
                print("wrong")
        else:
            print("it is not entered")
    else:
        print("u have not generated")
else:
    print("enter the 10 digit number")