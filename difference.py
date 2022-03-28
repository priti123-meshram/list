list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
a=[]
i=0
while i<len(list1):
    k=list1[i]
    if k not in list2:
        a.append(k)
    i=i+1
print(a)
