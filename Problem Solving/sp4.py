password = input()

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

num = 0
lc = 0
uc = 0
sc = 0
count=0

for i in numbers:
    if i in password:
      num+=1

for j in lower_case:
    if j in password:
        lc+=1

for k in upper_case:
    if k in password:
        uc+=1

for m in special_characters:
    if m in password:
        sc+=1


if num==1 and lc==1 and uc==1 and sc==1:
    if len(password)<6:
        print(2)
else:
        if num==0:
            count+=1
        if lc==0:
            count+=1
        if uc==0:
            count+=1
        if sc==0:
            count+=1

        if count==0:
            print(6)
        if count==1:
            print(5)
        if count==2:
            print(4)
        if count==3:
            print(5)
        if count==4:
            print(2)
        if count==5:
            print(1)


