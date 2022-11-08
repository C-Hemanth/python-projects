n=25
k=5
count=0
i=0
while i<6:
    for j in range(1,6):
        print(j)
        count=count+1
        print(count)
        if n== count:
            print(j)
            if j==k:
                print('s')
            else:
                # print('no')
                pass
        else:
            pass
    i=i+1