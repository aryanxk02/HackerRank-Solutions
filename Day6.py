n = int(input())

odd = []
even = []

for i in range(n):
    string = input()
    
    for j in range(0, len(string), 2):
        odd.append(string[j])

    for k in range(1, len(string), 2):
        even.append(string[k])

    print(str(''.join(odd))+str(' ')+str(''.join(even)))

    odd.clear()
    even.clear()