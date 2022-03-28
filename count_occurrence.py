n = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
a=[]
for i in n:
    if i not in a:
        a.append(i)
print(a)
i=0
while i<len(a):
    count=0
    for j in range(0,len(n)):
        if a[i]==n[j]:
            count=count+1
    print(a[i], "=",count)
    i=i+1

