lst= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=[]
d=[]
c1=0
c2=0
avg1=0
sum2=0
sum1=0
avg2=0
while i<len(lst):
    b=lst[i]
    if b%2==0:
        c.append(b)
        c1=c1+1
        sum1=sum1+b
    else:
        d.append(b)
        c2=c2+1
        sum2=sum2+b
    i=i+1
avg1=sum1/c1
avg2=sum2/c2
print("the count of even nunber is : ",c,avg1)
print("the count of odd number is: ",d,avg2)


