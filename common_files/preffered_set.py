nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Pref = 5

new_list=[]

def sum_of_numbers(a,b):
    return a+b
#Output(1, 4)(2, 3)(3, 2)(4, 1)
for i in range(len(nums)+1):
    print
    preferred_number = sum_of_numbers(nums[i],nums[i+1])
    print(preferred_number )
    #print(nums[i])
    #print(nums[i]+1)
    #pref_value = nums[i]+nums[i+1]
    #print(pref_value)
    #if (pref_value == 5 ):
       # new_list=new_list.append(nums[i])
        #new_list=new_list.append(nums[i+1])
    #print(new_list)

