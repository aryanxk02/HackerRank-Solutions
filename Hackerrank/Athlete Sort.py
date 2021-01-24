no_of_rows, no_of_columns = list(map(int, input().split()))

row_elements = [(input()) for i in range(0, no_of_rows)]

k = int(input())

for row_elements in sorted(row_elements, key=lambda row: int(row.split()[k])):
    print(row_elements)

