l= []
print("Enter Number of Elements");
n=int(input())
for i in range(0,n):
    l.append(int(input()))
prime=[]
for i in l:
    count=0
    
    for j in range(1,i+1):
        if i%j == 0:
            count=count+1
       
    if count==2:
        prime.append(i)
print(prime)

    
