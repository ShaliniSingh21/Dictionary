#d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3=dict(d1)
# d3.update(d2)
# for i ,j in d1.items():
#     for x,y in d2.items():
#             if i==x:
#                 d3[i]=(j+y)
# print(d3)
data=[{"V":"S001"}, {"V": "S002"}, {'VI': "S001"}, {"VI": "S005"},
{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
l=[]
i=0
while i<len(data):
    for j in data.values():
        if data[i] not in l:
            l.aapend(data[i])
    i=i+1
print(data[l])    
            

        


