n = int(input())
dictionary = {}
for i in range(0, n):
    inputArray = input().split()
    marks = list(map(float, inputArray[1:]))
    print(marks)
    dictionary[inputArray[0]] = sum(marks)/len(marks)
print("%.2f" % dictionary[input()])


