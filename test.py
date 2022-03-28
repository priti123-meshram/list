# n=input("enter the name")
# t=list(n)
# # print(t)
# rev=list(n)
# rev.reverse()
# if t==rev:
#     print("it is polindrome ",rev)
# else:
#     print("it is not polindrome",rev)


# a=input("enter the palindrome")
# i=0
# b=a[-1::-1]
# if (a==b):
#     print("it is palindrome",a)
# else:
#     print("it is not palindrome",a)

n=input("enter the polindrome number")
c=list(n)
b=[]
i=1
while i<=len(n):
    b.append(n[-i])
    i+=1
if c==b:
    print("it is polindrome ",b)
else:
    print("not",b)

    



    
