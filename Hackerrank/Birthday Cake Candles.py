#n= int(input())
#a = list(map(int, input().split()))
#sum = 0
#for i in range(0, n):
  #  if a[i] == max(a):
 #       sum = sum + 1
#print(sum)
#_________________________________________________________

#def birthdayCakeCandles(arg):

   # sum = 0
    #for i in range(0, n):
     #   if arg[i] == max(arg):
      #      sum = sum + 1
    #print(sum)
#n = int(input())
#arg = list(map(int, input().split()))
#birthdayCakeCandles(arg)

#______________________________________________________
#def add(a,b):
 #   c = a+b
  #  print(c)

#x= int(input())
#y = int(input())
#add(x, y)
#_______________________________________________________
def birthdayCakeCandles(l):
    print(l.count(max(l)))
n = int(input())
l = list(map(int, input().split()))
birthdayCakeCandles(l)
