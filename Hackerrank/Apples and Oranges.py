s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
pos_of_apples = list(map(int, input().split()))
pos_of_oranges = list(map(int, input().split()))
number_of_apples = 0
number_of_oranges = 0

for i in range(0, m):
    if a+pos_of_apples[i]>=s and a+pos_of_apples[i]<=t:
        number_of_apples+=1
    else:
     pass
for j in range(0, n):
    if b+pos_of_oranges[j]>=s and b+pos_of_oranges[j]<=t:
        number_of_oranges+=1
    else:
        pass
print(number_of_apples)
print(number_of_oranges)


