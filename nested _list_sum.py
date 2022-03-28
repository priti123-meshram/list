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



# n=[1,2,[3,4,5],[6,7,8,9,10,11]]
# i=0
# sum=0
# while i<len(n):
#     b=n[i]
#     if type(b)==list:
#         for j in range(len(b)):
#             sum=sum+b[j]
#     else:
#         sum=sum+n[i]
#     i=i+1
# print(sum)


