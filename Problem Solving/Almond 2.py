n = int(input())
count = 0
if n % 2 == 0:
    dum = True
    while dum:
        n = int(n/2)
        count += 1
        if n % 2 == 1:
            count += 1
            print(count)
            dum = False
        elif n %
elif n % 2 == 1:
    while True:
        n = int(n/2)
        count += 1
        if n == 1:
            count+= 1
            print(count)
            break

# n = int(input())
# x = 0
# count = 0
# dummy = True
# while dummy:
#     n = int(n/2)
#     # print('n ;', n)
#     # print(type(n))
#     count += 1
#     if (n)%2 == 1:
#         count += 1
#         dummy = False
#         break
# print(count)
# # print(int(3/2))