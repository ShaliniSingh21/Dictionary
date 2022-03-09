students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
l={}
k={}
for i in students.values():
    for j in students.values():
        l.update(students[i])
        k.update(students[j])
print(l,k)


