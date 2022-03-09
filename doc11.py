dict={'age':'normal',"pet":'dog'}
dict1={1:10, 2:20}
dict2={'shalini':'omm','daksh':'betu'}
l={}
for i in dict1,dict2,dict:
   # for j in dict2:
        l.update(i)
print(l)     