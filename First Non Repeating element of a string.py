a=input("Enter the string: ")
temp=""
for i in range(0,len(a)-1):
    flag=0
    temp=a[i]
    for j in range(i+1,len(a)-1):
        
        if temp== a[j]:
            flag=1
    
    if flag==0:
        print(a[i+1])
        exit()
    
    
