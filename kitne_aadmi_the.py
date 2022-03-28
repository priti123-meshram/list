
lst= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=0
d=0
while i<len(lst):
    if lst[i]%2==0:
        c=c+1
    else:
        d=d+1
    i=i+1
print("the count of even nunber is : ",c)
print("the count of odd number is : ",d)