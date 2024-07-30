#  constructor 

# class Student:
#     x=10
#     y=20
   
#     def __init__(self,x):
#         print(" gm ")
              
#     def __init__(self,x,y):
#         print(" hello ")
              
#     def __init__(self,x,y,z):
#         print("hi ")
              
    

# obj=Student(10,20,333)

#  variable

#  instance variable decleare through constructor

# class student:
#     # def __init__(self,name,age):
#     #     self.n1=name
#     #     self.n2=age
#     def display(self):
#         print(" Name = ", self.n1)
#         print("Age=", self.n2)

# obj1=student()
# # obj1=student('Raj',25) 
# # obj1.display()  
# # print(obj1.n1)
# # print(obj1.n2)

# obj1.n1="raj"
# obj1.n2=25
# obj1.display()

# instance variable declaration through instance method

class Student:
    def display(self,name,age):
        self.n1=name
        self.n2=age
    def Show(self):
        print(self.n1,self.n2)

obj=Student() 
obj.display('raj',25)
obj.Show()
print(obj.n1,obj.n2)


#  access instance variable:

#  1. within the class->through self
#  2. outside of the class-> through object













