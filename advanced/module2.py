# from module1 import add,x,y
# print(x,y)

# p=add(x,y)
# print(p)

# from module1 import add as a,x,y
# print(x,y)
# p=a(x,y)
# print(p)

#  

def outerfun(fun):
    def innerfun(x,y):
        x=x+10
        y=y+10

        return fun(x,y)
        
        print("main function call")
    return innerfun  
@outerfun
def main (x,y):
    return x+y
x=main(5,5)
print(x)
       


    


