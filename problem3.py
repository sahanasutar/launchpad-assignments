a=[1,2,3,2,0,65,10,88,52,7,9,2]
b=[]
for i in range(len(a)):
    if a[i]==2:
        b.append(i)
list(b)