# num = int(input())
# x = [num]
# count = 1
# j = []
# while num>0:
#     num = num-count
#     count += 1
#     if num>0:
#         j.append(num)
#     print('num:', num)
# print(x[0]-min(j))
s = 'lj'
x = []
for i in range(len(s)):
    count = 1
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            print('s[i]:', s[i])
            print('s[j]', s[j])
            count += 1
        else:
            break
    x.append(count)
print(x)
if x[:] == 1:
    print(0)
else:
    print(max(x))

# class Solution {
# public:
#     int maxPower(string s) {
#         vector <int> x;
#         for (int i=0; i<x.size(); i++){
#             int count = 1;
#             for (int j=i+1; j<x.size(); j++){
#                 if (s[i]==s[j]){
#                     count++;
#                 }
#                 else{
#                     return;
#                 }
#             }
#             x.push_back(count);
#         }
#         for i
#     }
# };