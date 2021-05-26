num = int(input())
total = 0
q = num//10
while total<10:
    q = num // 10
    r = num % 10
    total += r
    num = q
    print('num:',num)
    print('total:', total)
print(total)
