n = int(input())

for _ in range(n):
    count = 0

    students, threshold = input().split()
    students = int(students)
    threshold = int(threshold)

    array = list(map(int, input().split()))

    for i in array:

        if i <= 0:
            count += 1

    if count >= threshold:
        print('NO')
    else:
        print('YES')