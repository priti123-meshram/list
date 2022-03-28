n=int(input("enter the num"))
i=(n)
rev=0
while i>0:
    remainder=i%10
    i//=10
    rev=rev*10+remainder
if n==rev:
    print("it is palindrome",n)
else:
    print("it is not palindrome",n)







# n=input("enter the polindrome number")
# c=list(n)
# b=[]
# i=1
# while i<=len(n):
#     b.append(n[-i])
#     i+=1
# if c==b:
#     print("it is polindrome ",b)
# else:
#     print("not",b)

    

