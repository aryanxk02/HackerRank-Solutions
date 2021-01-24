number = int(input())
n = input()

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# pass : A3f#

num = 0
lcase = 0
ucase = 0
s_char = 0
count=0

for i in n:
    if i in numbers:
       num+=1
    elif i in lower_case:
        lcase+=1
    elif i in upper_case:
        ucase+=1
    else:
        s_char+=1

if num==0:
    count+=1
if lcase==0:
    count+=1
if ucase==0:
    count+=1
if s_char==0:
    count+=1

if( (ucase+lcase+num+s_char+count) < 6 ):
    count=count+(6-(ucase+lcase+num+s_char+count))
print(count)
----------------------------------
number = int(input())
n = input()


numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# pass : A3f#

num = 0
lcase = 0
ucase = 0
s_char = 0
count=0

for i in n:
    if i in numbers:
       num+=1
    elif i in lower_case:
        lcase+=1
    elif i in upper_case:
        ucase+=1
    else:
        s_char+=1
if(len(n)<6):
    print(6-len(n))
elif num==0:
    print("1")
elif lcase==0:
    print("2")
elif ucase==0:
    print("3")
elif s_char==0:
    print("4")
else:
    print("")