str =input("Enter Sring : ")
list1=[]
c=0
i=0
for j in str:
    i=i+1
    if j=='a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' or j=='A' or j == 'E' or j == 'I' or j == 'O' or j == 'U' :
       list1.append(j)
       c=c+1
print(list1)
print("Count of Vowel is : ",c)
print("Count of String is : ",i)
