n = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
a=0
b=0
c=0
count1=0
count2=0
count3=0
for i in n:
    n=[i]    
    if a>=1000000:
        count1=count1+1
    elif b>=100000:
        count2=count2+1
    elif c<=99999:
        count3=count3+1
        i=i+1
print("it is crorepati",count1)
print("it is lakhpati",count2)
print("it is dilwale",count3)