n = int(input('Enter number of students :'))

arr = []
original_list = []
print('Enter marks')


for i in range(n):
    marks = int(input())
    original_list.append(marks)
    if marks >= 0:
        arr.append(marks)

def average(arr):
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]
    return total/len(arr)

def maximum(arr):
    max_score = arr[0]
    for i in arr:
        if i > max_score:
            max_score = i
    return max_score

def minimum(arr):
    min_score = arr[0]
    for i in arr:
        if i < min_score:
            min_score = i
    return min_score

def high_freq(arr):
    freq = 0
    for i in arr:
        if arr.count(i) > freq:
            freq = arr.count(i)
            value = i
    return value

print('Marks :', original_list)
print('Number of students absent for the test :', len(original_list) - len(arr))
print('Average score:', average(arr))
print('Maximum score :', maximum(arr))
print('Minimum score :', minimum(arr))
print('Highest Frequency :', high_freq(arr))