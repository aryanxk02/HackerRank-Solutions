def pairs(arr, m):
    set1 = set(arr)
    set2 = [num + m for num in arr]
    print(len(set1.intersection(set2)))
n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split()))
n = int(n)
m = int(m)
pairs(arr, m)