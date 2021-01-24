n = int(input())
all_marks=[]

for marks in range(n):
    marks = int(input())

    if marks>=38:

        if marks%5>=3:
            marks=marks+5-(marks%5)
            all_marks.append(marks)
        else:
            all_marks.append(marks)

    if marks<38:
        all_marks.append(marks)

for i in all_marks:
    print(i)