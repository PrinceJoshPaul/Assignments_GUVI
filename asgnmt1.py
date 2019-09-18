a=[3,5,[3,56],3,[3,7,'zen',4.6],'guvi',5,2,'pit']
c=0
max=0
for i in a:
    if isinstance(i,list):
        c+=1
        if max < len(i):
            max=len(i)
            index=a.index(i)
print(len(a))
print("no of sublists in the list:",c)
print("The sublist with the max length:",a[index])
print("The index of sublist with max length:",index)
print("The 1st element of the sublist with max length:",a[index][0])
