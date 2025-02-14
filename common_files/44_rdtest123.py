input_string = "this is my world"
output_string = "YM DLROW SIHT SI"

temp_string_split=input_string.split(" ")
new_list = list(temp_string_split);
#print(new_list)
#print(new_list[1])

def reverse_string(reverse_it):
    return reverse_it[::-1]

upper_case_list=[];
for i in new_list:
    #print(type(i))
    #str(i)
    reversedString= reverse_string(i)
    print(reversedString)
    print(reversedString.upper())
    upper_case_list.append(reversedString.upper())

print(upper_case_list)

print("rd".join(upper_case_list))



#text = new_list[1];
#text = "Hello"[::-1]
#print(text)

#reverse_string(new_list)




#def reverse_string():



