number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
a=[]
i=0
while i<len(n):
    if n[i]+n[-i]==number:
        k=(n[i],n[-1])
        a.append(k)
    i=i+1
print(a)

