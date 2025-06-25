t=int(input())
list=[]
for i in range(1,10000):
    if i%10!=3 and i%3!=0:
        list.append(i)
for p in range (t):
    b=int(input())
    print (list[b-1])
