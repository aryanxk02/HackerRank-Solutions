n = int(input())

l = []

for i in range(n):
    widget_count = int(input())
    l.append(widget_count)

total = int(input())

count = 0
x = 0

for order in l:
    if order!=0 and x+order<=total:
            x = x + order
            count += 1

print(count)