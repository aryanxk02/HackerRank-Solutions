t = int(input())
for _ in range(t):
    g = int(input())
    for _ in range(g):
        arr = list(map(int, input().split()))
        # x = [i for i in range(1, arr[1]+1)]
        # odd = 0
        # for j in x:
        #     if j%2==0:
        #         odd += 1
        # if arr[2] == 1:
        #     print(odd)
        # elif arr[2] == 2:
        #     print(len(x)-odd)
        if arr[1]%2==0:
            print(int(arr[1]/2))
        else:
            if arr[2]==arr[0]:
                print(int(arr[1]//2))
            else:
                print(int((arr[1]+1)/2))
