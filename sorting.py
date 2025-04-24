# l=[4,10,48,80,2,35]
# print(l)
# for i in range(len(l)):
#     m=i
#     for j in range(i+1,len(l)):                             #SELECTION SORT
#         if l[m]>l[j]:
#             m=j
#     l[i],l[m]=l[m],l[i]
# print(l)

# [4, 10, 48, 80, 2, 35]
# [2, 4, 10, 35, 48, 80]


import math

l=[3,7,1,34,567,8,5,8,6,4]
num_of_buckets = round(math.sqrt(len(l)))
max_ele =max(l)
bu =[]


for i in range(num_of_buckets):
    bu.append([])
    
for j in l:
    sd=math.ceil((j*num_of_buckets)/max_ele)
    
print(bu)
print(num_of_buckets)