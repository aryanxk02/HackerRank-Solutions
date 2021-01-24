def beautifulDays(i, j, k):
    count = 0
    for number in range(i, j+1):
        l = []
        for digit in str(number):
            l.append(digit)
        l.reverse()
        l = int(''.join(l))
        # print(f'number : {number}')
        # print(f'reverse : {l}')
        if abs(number-l)%k==0:
            count+=1
    print(count)

        # if abs(i-int(''.join(l)))%k==0:
        #     count+=1
    # print(count)

i, j, k = list(map(int, input().split()))
beautifulDays(i, j, k)

# l = ['1', '2']
# print(''.join(l))