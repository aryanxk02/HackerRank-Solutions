budget, keyboard, usb = input().split()

budget = int(budget)
keyboard = int(keyboard)
usb = int(usb)

keyboards_costs = list(map(int, input().split()))
usb_costs = list(map(int, input().split()))

total_cost = 0
l = []

for i in keyboards_costs:
    for j in usb_costs:
        l.append(i+j)

for k in l:
    if max(l)>budget:
        l.remove(max(l))

if l == [] :
    print(-1)
else:
    print(max(l))

# Approach-2

# budget, keyboard, usb = input().split()
#
# budget = int(budget)
# keyboard = int(keyboard)
# usb = int(usb)
#
# keyboards_costs = list(map(int, input().split()))
# usb_costs = list(map(int, input().split()))
#
# total_cost = 0
# l = []
#
# for i in keyboards_costs:
#     for j in usb_costs:
#         if (i + j)<=budget :
#             l.append(i + j)
#
# if l == []:
#     print(-1)
# else:
#     print(max(l))