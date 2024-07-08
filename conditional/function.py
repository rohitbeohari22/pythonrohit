# def add(x,y,z):
#     print(x+y+z)
# p=int(input("Enter first no: "))   
# q=int(input(" Enter second no :")) 
# r=int(input("Enter third no :"))

# add(p,q,r)

# x=add(p,q,r)
# print(x)

def add(x,y):
    return x+y,x-y,x*y,x/y,x%y,x//y

p=int(input(" Enter first no :"))
q=int(input("Enter second no:"))

a,b,c,d,e,f=add(p,q)
print(a,b,c,d,e,f)

