# n=[1,2,2,3,1,2,5,4,1]
# a=[]
# for i in n:
#     if i not in a:
#         a.append(i)
# print(a)
# i=0
# while i<len(a):
#     count=0

#     for j in range(0, len(n)):
#         if a[i]==n[j]:
#             count+=1
#     c=count%2
#     print(a[i],"=",c)
#     i=i+1


# n=[1,2,2,3,1,2,5,4,1,5]
# a=[]
# for i in n:
#     if i not in a:
#         a.append(i)
# print(a)
# i=0
# while i<len(a):
#     j=0
#     count = 0
#     while j<len(n):
#         if n[i]==n[j]:
#             count+=1
#         j+=1
#     print(n[i],"=",count)
#     i+=1

n=[1,2,2,3,1,2,5,4,1,5,5,5,4,2]
a=[]
for i in n:
    if i not in a:
        a.append(i)
print(a)
i=0
while i<len(a):
    count = 0
    for j in range (0,len(n)):
        if a[i]==n[j]:
            count+=1
    print(a[i],"=",count//2)
    i+=1



    
    



