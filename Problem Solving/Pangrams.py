def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True

string = input().strip()
if(ispangram(string) == True):
   print("pangram")
else:
   print("not pangram")