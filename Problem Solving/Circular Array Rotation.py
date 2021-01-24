def circularArrayrotations(n, k, q):
    array = list(map(int, input().split()))  # 1 2 3
    temp = []

    for _ in range(k):
        temp.append(array[-1])
        array.remove(array[-1])
        array = temp + array
        temp = []

    for i in range(q):
        print(array[int(input())])

n, k, q = list(map(int, input().split())) # n = number of elements, k = number of rotations, q = test cases
circularArrayrotations(n, k, q)