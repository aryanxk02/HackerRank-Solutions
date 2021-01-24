# n = int(input())
# x = list(map(int, input().split()))
# y = 0
# for i in range(0, len(x), 2):
#     y += x[i]
# # print(y)
# if y == sum(x)/2:
#     print(sum(x))
# else:
#     print(sum(x)-(y-(sum(x)-y)))
n = int(input())
x = list(map(int, input().split()))
odd = 0
even = 0
for i in range(len(x)):
    if i%2 == 0:
        even += x[i]
    else:
        odd += x[i]
while(even!=odd):
    if even>odd:
        even -= 1
    elif even<odd:
        odd -= 1
print(even*2)
