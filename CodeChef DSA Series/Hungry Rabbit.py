rabbit = list(map(int, input().split()))
carrot = []
dist = []
for _ in range(4):
    carr_arr = list(map(int, input().split()))
    carrot.append(carr_arr)
print(carrot)
print(rabbit)
# print(carrot[2][0])
for i in range(len(carrot)):
    dist.append([abs(carrot[i][0] - rabbit[0]), abs(carrot[i][0] - rabbit[1])])
print(dist)
