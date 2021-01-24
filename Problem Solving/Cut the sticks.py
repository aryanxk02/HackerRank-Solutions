n = int(input())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while len(arr)!=0:
    print(len(arr))
    arr = [x for x in arr if x != min(arr)]