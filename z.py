data = '04122000'
datalist=[]
for i in data:
    datalist.append(i)
for i in range(len(datalist)):
    
    if i == 2:
        datalist[2]='/'+datalist[2]
    if i == 4:
        datalist[4]='/'+datalist[4]
    print (datalist[i])
data = ''.join(datalist)
print(data)