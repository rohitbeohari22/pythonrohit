my_set={10,30,60,20,40}
print(my_set)

print(len(my_set))
print(max(my_set))
print(min(my_set))

my_set.add(50)
print(my_set)

my_list=[10,20,10,20,10,20]
my_set.update(my_list)
print(my_set)

my_set.remove(30)
print(my_set)

my_set.discard(20)
print(my_set)

s1={10,20,30}
s2={40,50,10}

s3=s1.intersection(s2)
print(s3)

s4=s1.union(s2)
print(s4)




s5=s1.difference(s2)
print(s5)