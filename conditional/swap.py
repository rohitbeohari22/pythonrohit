# WAp to swap two variable values third variable.

# x=10
# y=20
# print("before swap ", x,y)

# z=x
# x=y
# y=z
# print("after swap ",x,y)


# x=int(input("Enter first no :"))
# y=int(input("Eneter second no:"))

# print("Before swap :",x,y)
# x=x*y
# y=x/y
# x=x/y

# print("after swap :",x,y)


# x=int(input("enter first no:"))
# y=int(input("enter second no:"))

# print("before swap :",x,y)
# x=x+y
# y=x-y
# x=x-y
# print("after swap :",x,y)




# x=int(input("enter first no:"))
# y=int(input("enter second no:"))

# print("before swap :",x,y)
# x,y=y,x
# print("after swap :",x,y)



# armstrnong

n=int(input("enter eny no:"))
m,p=n,n
count=0
sum=0

while n>0:
    count=count+1
    n=n//10
print("count =",count)   

while m>0:
    digit=m%10
    sum=sum+digit**count
    m=m//10
if sum==p:
    print("armostrong yes")
else:
    print("armstong no")

        




