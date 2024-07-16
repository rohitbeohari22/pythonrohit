# map
# Wap to program squar or any collection 

# my_list=[1,2,3,4,5]

# def squar(n):
#     return n**2
# new_list=list(map(squar,my_list))
# print(new_list)

#WAP to find addtion of 2 list on the bases of indexing 

# my_list1=[1,2,3,4,5]
# my_list2=[5,4,3,2,1]

# def add(x,y):
#     return x+y

# new_list=list(map(add,my_list1,my_list2))
# print(new_list)

# def add(x,y):
#     return x+y

# # 
# new_list=list(map(add,(1,2,3,4),(1,2,3,4)))
# print(new_list)


# #  
# x=lambda a,b:a+b
# print((list(map(x,[1,2,3,4],[2,4,6,8]))))

#  0-9      asqi(48-57)
#  A-Z          (65-90)
#  a-z          (97-122)


#  filter

# my_list=[20,30,40,50,60]

# def new(n):
#     if n>=30:
#         return True
# print(list(filter(new,my_list)))    


# reduce
import functools
my_list=[20,25,45,55]
def smallest(x,y):
    if x<y:
        return x
    else:
        return y
print(functools.reduce(smallest,my_list))   
    