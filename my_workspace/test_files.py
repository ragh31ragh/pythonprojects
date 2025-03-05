import os
#os.path.curdir
#print("test")
#print("hello world")

#print the numbers, where count is more than 2
abc = "99679987434456"
new_list= list(abc)
print(new_list)
updated_list=[]
for i in range(len(new_list)):
    print(new_list[i])
    print(type(new_list[i]))
    updated_list.append(int(new_list[i]))
    #if *new
print(updated_list)

def number_of_digits(some_list):
    counting = 0
    for ij in range(len(updated_list) - 1):
        if some_list[ij] == some_list[ij+1]:
            counting = counting + 1
    return counting;



more_than_two_list = []
count = 0
for j in range(len(updated_list)-1):
    #count=0
    if updated_list[j] == updated_list[j+1]:
        count = count + 1 ;



print(count+1)