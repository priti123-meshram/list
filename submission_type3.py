n = [
    [8, 3, 4],
    [1, 6, 9],
    [6, 7, 2]
]
i=0
while i<len(n):
    j=0
    sum=0
    while j<len(n):
        sum=sum+n[i][j]
        j=j+1
    i=i+1
print(sum)
r=0
while r<len(n):
    k=0
    sum1=0
    while k<len(n):
        sum1=sum1+n[r][k]
        k=k+1
    r=r+1
print(sum1)

        
