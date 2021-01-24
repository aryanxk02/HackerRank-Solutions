n = input()
a = list(n)

# aaabcddd abcddd abcd

# aaacccdddvvvv acccdddvvvv acdddvvvv acdvvvv acdvv acd

i=0
while 0<=i<len(a)-1:
    if a[i]==a[i+1]:
        del a[i]
        del a[i]
        i=0
    else :
        i=i+1
if a == []:
    print('Empty String')
else:
    print(''.join(a))





