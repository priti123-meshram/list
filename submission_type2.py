n=[1,2,2,5,8,4,4,8]
a=[]
count=0
i=0
while i<len(n):
    # b=a[i]
    b= i not in a
    a.append(b)
    count =count+1
    i=i+1
print(count)