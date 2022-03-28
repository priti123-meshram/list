# print("welcome to kbc")
# print("kon banega krorpati")
# question_list = ["1).How many continents are there?",  

#                 "2).What is the capital of India?", 

# 				"3).NG mei kaun se course padhaya jaata hai?"]


# options_list = [["1.four","2.nine","3.seven","4.eight"],

#                ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],

#                ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]

# solution = [3, 4,1]

# answer=["3.seven","4.eight","3.chennai","4.delhi" "1.software engineering","2.counseling"]
# i=0
# amount = 1000
# count = 0
# b=0
# a=0
# while i<len(question_list):
#     print(question_list[i])
#     j=0
#     k=1
#     while j<=len(options_list[i]):
#         print(options_list[i][j])
#         j=j+1
#         lifeline=input("do you want lifeline")
#         if lifeline=="yes":
#             print("5050")
#             if count==5050:
#                 print(answer[b+i])
#                 print(answer[b+a])
#                 num=int(input("enter the answer"))
#                 if num==solution[i]:
#                     print("your answer is right")
#                     print("you won",amount,"$")
#                 else:
#                     print("answer is wrong")
#                     print("you loose the game")
#                     break
#                 count=count+1
#                 print()
#             else:
#                 print("you had already used lifeline")
#                 e=int(input("enter the answer"))
#                 if e==solution[i]:
#                     print("your answer is right")
#                     print("you won",amount,"$")
#                 else:
#                     print("answer is wrong")
#                     print("you loose the game")
#                     break
#                 count=count+1
#                 print()
#     else:
#         f=int(input("enter the answer"))
#         if f == solution[i]:
#             print("your answer is right")
#             print("you won",amount,"$")
#         else:
#             print("answer is wrong")
#             print("you loose the game")
#             break
#         print()
#     amount=amount+1000
#     i=i+1
#     a=a+1
#     b=b+1




print("welcome to kbc")
print("kon banega krorpati")
question_list=[
    "how many continents are there ?",        # pehla question
    "what is the capital of india?",          # dusra question
    "Ng mei kon se course padhaya jaata hai",  #teesra question
]
option_list=[
    ["Four", "nine", "seven", "Eight"],#first option
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],#second option
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],#third option
]
# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list=[3,4,1]
ans=["seven","delhi","software engineering"]
i=0
count=0
while i<len(question_list):
    m=question_list[i]
    print(m)
    j=0
    k=i
    while j<len(option_list[k]):
        d=option_list[k][j]
        print(j+1,option_list[k][j])
        j=j+1
    user_input=input("do you using lifeline :-  ")
    if user_input=="yes":
        print("5050")
        if count==0:
            print(option_list[i][i])
            print(ans[i])
            a=int(input("only now time using lifeline :-  "))
            if a==2:
                print("..your answer is correct..\n")
                count=count+1
            else:
                print("you ans is wrong")
                break
        else:
            print("you can't use more lifeline")
            b=int(input("choose the answer :-  "))
            if b==solution_list[i]:
                print("..your ans is correct..\n")
            else:
                print("your ans is wrong")
                break
    else:
        c=int(input("choose the answer :-  "))
        if c==solution_list[i]:
            print("..your answer is correct..\n")
        else:
            print("..your answer is wrong..")
        i=i+1