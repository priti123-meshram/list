n=input("enter the alphbet")
for i in n:
    if n>="a" or n<="z":
        print(n)
        char=input("enter the char")
        if char=="#" or char=="@" or char=="&":
            print(char)
            num=int(input("enter the num"))
            if num>=0:
                print(n+char+str(num))
                break
            else:
                print("no")
        else:
            print("its not char")
    else:
        print("this is not alphabet")



# n=input("enter the alphbet")
# i=1
# while i<len(n):
#     if n>="a" or n<="z":
#         print(n)
#         char=input("enter the char")
#         if char=="#" or char=="@" or char=="&":
#             print(char)
#             num=int(input("enter the num"))
#             if num>=0:
#                 print(n+char+str(num))
#                 break
#             else:
#                 print("no")
#         else:
#             print("its not char")
#     else:
#         print("this is not alphabet") 
#     i+=1           

