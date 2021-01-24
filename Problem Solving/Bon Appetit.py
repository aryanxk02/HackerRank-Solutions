no_of_items, item_no = input().split()
no_of_items = int(no_of_items)
item_no = int(item_no)

l = list(map(int, input().split()))
amnt_charged = int(input())

l.remove(l[item_no])

if sum(l)/2==amnt_charged:
    print('Bon Appetit')
else:
    print(int(amnt_charged-sum(l)/2))