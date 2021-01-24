a = list(map(int, input().split()))
#max value = sum of list - lowest number
#min value = sum of list - max number
max_a = max(a)
min_a = min(a)
sum_a = sum(a)
print(sum_a-max_a, sum_a-min_a)