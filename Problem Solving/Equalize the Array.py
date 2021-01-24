n = int(input())
array = list(map(int, input().split()))
print(len(array)-array.count(max(array)))