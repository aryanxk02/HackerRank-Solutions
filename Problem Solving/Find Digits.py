testcase = int(input())

for t in range(testcase):
    n = str(input())
    digit = []
    count = 0

    for char in n:
        digit.append(char)

    for i in digit:
        if int(i) != 0:

            if int(n) % int(i) == 0:
                count += 1

    print(count)


    digit = []




