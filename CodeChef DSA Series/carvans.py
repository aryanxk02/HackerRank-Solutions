# 4 5 1 2 3
t = int(input())
for i in range(t):
    count = 1
    no_cars = int(input())
    speeds = list(map(int, input().split()))
    for i in range(1, len(speeds)):
        if speeds[i] < speeds[i-1]:
            count += 1
        else:
            speeds[i] = speeds[i] - (abs(speeds[i]-speeds[i-1]))
    print(count)