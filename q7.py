dic=[{"first":"1"}, {"second": "2"},{"third": "1"}, {"four": "5"}, 
{"five":"5"},{"six":"9"},{"seven":"7"}]
i=0
l=[]
while i<len(dic):
    for j in dic[i]:
        if dic[i][j] not in l:
            l.append(dic[i][j])
        i=i+1
print(l)            

                  

# dic=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"}, 
#      {"six":"9"},{"seven":"7"}]
# l=[]
# i=0
# while i<len(dic):
#     for j in dic[i]:
#          if dic[i][j] not in l:
#              l.append(dic[i][j])
#           i=i+1
# print(l)        
                          