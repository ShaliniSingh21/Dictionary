# dict={'no1':34,'no2':73,'no3':38,'no4':53,'no5':43}
# l=[]
# max1=0
# max2=0
# max3=0
# for i in dict:
#     for j in dict[i]:
#         if dict[i]>max1:
#             max1=dict[i]
#         elif dict[i]>max1 and dict[i]>max2:
#             max2=dict[i]
#         elif dict[i]>max2 and dict[i]>max3:
#             max3=dict[i]
# l.append(max1)              
# l.append(max2)
# l.append(max3)
# print(l)


    
dict={'no1':34,'no2':73,'no3':38,'no4':53,'no5':43}
l=[]
max1=0
max2=0
max3=0
for i in dict:
    if dict[i]>max1:
        max1=dict[i]   
for i in dict:
    if dict[i]>max2:
        max2=dict[i]
    elif dict[i]>max3:
        max3=dict[i]
print(max3)    