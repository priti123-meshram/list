# n = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# max=0
# while i<len(n):
#     a=n[i]
#     if a>max:
#         max=a
#     i=i+1
# print(max)


# n = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# max=0
# while i<len(n):
#     a=n[i]
#     if a>max:
#         max=a
#     i=i+1
# print(max)



n=[50,40,23,70,56,12,5,10,7]
a=0
b=0
for i in n:
    if i > a:
        a=i
# print(a)
n.remove(a)
a=0
c=0
for i in n:
    if i > c:
        c=i
print(c)


