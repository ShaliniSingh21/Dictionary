dict={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
empty={}
for i in dict:
    for j in dict.values():
        if dict[i]==' ':
            dict[i].pop(' ')
        # if dict[j]==' ':
        #     dict[j].pop(' ')
            empty.update(dict[i])
print(empty)            
