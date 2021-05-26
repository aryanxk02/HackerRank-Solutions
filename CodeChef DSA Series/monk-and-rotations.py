'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for i in range(t):
    x = list(map(int, input().split()))
    size = x[0]
    rotations = x[1]
    arr = list(map(int, input().split()))
    final = []
    for i in range(len(arr)-rotations, len(arr)):
        final.append(arr[i])
    for i in range(0, len(arr)-rotations):
        final.append(arr[i])
    # final.append(arr[len(arr)-rotations:len(arr)])
    # final.append(arr[:len(arr)-rotations])
    print(*final)
