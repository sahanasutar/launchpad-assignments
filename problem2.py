def elements_lessthan_five(l):
    l1=[]
    for i in l:
        if i<5:
            l1.append(i)
    return(l1)
print(elements_lessthan_five([21,6,17,5,3,8,6,5,72,0,3,64,2]))
    