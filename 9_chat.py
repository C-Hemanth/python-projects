class chat():
    bot='whatsapp'
    def __init__(self,hi,greeting):
        self.hi=hi
        self.greeting=greeting
    def chating(self):
        print(f"the reply is {self.hi}")
        print(f"{self.greeting}")
# c=chat('hello','good mornung')
c=chat()
# c=input("enter")
c.chating()
# print(c.hi)