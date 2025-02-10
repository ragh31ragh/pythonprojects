my_list=['a','b','c','d','e']
my_order=[3,0,4,1,2]
new_list = []
print(type(new_list))
for i in my_order:
    new_list.append(my_list[i])

print(new_list)
