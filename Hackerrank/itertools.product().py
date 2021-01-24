A = list(map(int, input().split()))
B = list(map(int, input().split()))
l = (list((x, y) for x in A for y in B))
print(*(i for i in l))
# * unpacks the list
    
# APPROACH 2
# print(*((x, y) for x in A for y in B))