
list2=[]
list3=[]
print("Enter size of list")
n=int(input())
for i in range(0,n):
    list2.append(int(input()))
print("Befor",list2)

for i in list2:
    if i not in list3:
        list3.append(i)
print("After removing Duplicate Values :",list3)
