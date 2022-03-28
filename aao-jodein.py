lst= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=[]
d=[]
sum1=0
sum2=0
while i<len(lst):
    b=lst[i]
    if b%2==0:
        c.append(b)
        sum1=sum1+b
        
    else:
        d.append(b)

        sum2=sum2+b
    i=i+1
print("the count of even nunber is : ",c,sum1)
print("the count of odd number is: ",d,sum2)


