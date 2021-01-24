import math
# approach 1

def compo(n):
        a, b = int(n[0]), int(n[2])
        print('Magnitutde :', math.sqrt(a**2+b**2))
        print('Phase :',math.atan(b/a))
n = list(input())
compo(n)


#approach 2
# import cmath
#
# r = complex(input().strip())
#
# print(cmath.polar(r))
# print(cmath.polar(r)[1])

 


