str1= "This is string \t we are creating new string"
#str1= "This is string \n we are creating new string"
print (str1)
print(len(str1))


str2="New standard collage"
print(str2[2:14])

str3="I am a coder"
print(str3.endswith("erd"))

print(str3.replace("a","B"))


str4=input("Enter your name:\n")
new_list=str4.split(" ");
new_str=str(new_list[0]);
print("Length of first name ")
print(len(new_str));
print("count of $ in first name ")
print(new_str.count("$"))

