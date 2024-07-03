n=int(input("Enter how many returned no you want : "))
i=1
sum=0
while i<=n:
    # print(i)
    sum=sum+i
    if i<=n-1:
     print(i,end="+")
    else:
     print(i,end=" = ")
    i=i+1
print(sum)
    
   