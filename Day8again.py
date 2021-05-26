# t = int(input())
# d = {}
# for _ in range(t):
#     inputArray = input().split(" ")
#     d[inputArray[0]] = inputArray[1]
# while True:
#     try:
#         k = input()
#         print(k+'='+d[k])
#     except:
#         print('Not found')
# n = int(input())
# name_numbers = [input().split() for _ in range(n)]
# phone_book = {k: v for k,v in name_numbers}
# while True:
#     try:
#         name = input()
#         if name in phone_book:
#             print('%s=%s' % (name, phone_book[name]))
#         else:
#             print('Not found')
#     except:
#         break
t = int(input())
d = {}
# for _ in range(t):
#     inputArray = input().split(" ")
#     d[inputArray[0]] = inputArray[1]
inputArray = [input().split() for _ in range(t)]
d = {x: y for x, y in inputArray}
while True:
    try:
        k = input()
        if k in d:
            print(k+'='+d[k])
        else:
            print('Not found')
    except:
        break