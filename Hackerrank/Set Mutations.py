n_A = int(input())
A = set(map(int, input().split()))
no_of_operations = int(input())

for i in range(no_of_operations):
    command = input().split()
    set_X = set(map(int, input().split()))
    if command[0]=='intersection_update':
        A.intersection_update(set_X) #je kahi intersection chi value asel ti vale A madhe update hoti
    elif command[0]=='update':
        A.update(set_X)
    elif command[0]=='symmetric_difference_update':
        A.symmetric_difference_update(set_X)
    elif command[0]=='difference_update':
        A.difference_update(set_X)
    else:
        pass
print(sum(A))