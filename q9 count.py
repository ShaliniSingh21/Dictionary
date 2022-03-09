l="MISSISSIPPI"
dic={}
for i in l:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)            
