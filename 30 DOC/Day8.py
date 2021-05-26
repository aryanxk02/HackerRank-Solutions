n = int(input())
d = {}

for i in range(n):

    inputArray = input().split()
    d[inputArray[0]] = int(inputArray[1])

    key_list = list(d.keys())
    value_list = list(d.values())
print(key_list)
for _ in range(n):

    try:
        k = d[input()]
        print(key_list[value_list.index(k)]+'='+str(int(k)))
    except:
        print('Not found')


