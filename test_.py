# n=[1,2,-3,4,-5,6,3,-7]
# a=[]
# for i in n:
#     if i<0:
#         a.append(-i)

# print(a)



# n=[1,2,-3,4,-5,6,3,-7,8,-9]
# a=[]
# for i in n:
#     if i<0:
#         a.append(0)
#     elif i>0:
#         a.append(i)
# print(a)


# list=[-1,9,7,-6,8,-4]
# i=0
# a=[]
# while i<len(list):
#     b=list[i]
#     if b<0:
#         a.append(0)
#     elif b>0:
#         a.append(b)
#     i=i+1
# print(a)




n=[1,4,5,[7,3,5,],[4,7,3]]
i=0
sum=0
while i <len(n):
    b=n[i]
    if type(b) is list:
        j=0
        while j<len(b):
            sum=sum+b[j]
            j+=1
    else:
        sum=sum+n[i]
    i=i+1
print(sum)
