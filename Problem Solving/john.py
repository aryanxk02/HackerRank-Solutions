x = list(map(int, input().split()))
b = x[0]
keyboard = list(map(int, input().split()))
usb = list(map(int, input().split()))
x = []
mx = 0
for i in keyboard:
    for j in usb:
        if i+j > mx and i+j <b:
            x.append(i+j)
            mx = i+j
# print(x)
# x.sort()
# if x[x.index(b)-1] < b:
#     print(x[x.index(b)-1])
# else:
#     print(-1)
if x==[]:
    print(-1)
else:
    print(x[-1])