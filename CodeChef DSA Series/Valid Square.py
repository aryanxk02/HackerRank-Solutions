p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]

d1 = ((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2)**0.5
d2 = ((p2[0] - p3[0])**2 + (p2[1] - p3[1])** 2)**0.5
d3 = ((p4[0] - p2[0])**2 + (p4[1] - p2[1])**2)**0.5
d4 = ((p1[0] - p4[0])**2 + (p1[1] - p4[1])**2)**0.5

diag1 = ((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2) ** 0.5
diag2 = ((p4[0] - p2[0]) ** 2 + (p4[1] - p2[1]) ** 2) ** 0.5

print('d1 :', d1)
print('d2 :', d2)
print('d3 :', d3)
print('d4 :', d4)

if d1 == d2 == d3 == d4 and diag1 == diag2:
    print(True)
else:
    print(False)