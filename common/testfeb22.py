numbers=input("Enter the numbers")
new_numbers=numbers.split(",")
print(list(numbers))
print(new_numbers)
for i in range(len(new_numbers)-1):
    #print(new_numbers[i])
    updated_list = [];
    if ( new_numbers[i] > new_numbers[i+1]):
        print(new_numbers[i])
        updated_list.append(new_numbers[i])
    else:
        updated_list.append(new_numbers[i])
    #elif(new_numbers[i] < new_numbers[i+1]):
        #print(new_numbers[i])
print(updated_list)