
calculation_of_units = 24;
name_of_unit = "hours";

def days_to_units(num_of_days):
    #print(f"{num_of_days} days are {num_of_days * calculation_of_units} {name_of_unit}");
    print("All good");
    return f"{num_of_days} days are {num_of_days * calculation_of_units} {name_of_unit}"

user_input = input("Enter number of days:\n");
user_input_number = int(user_input);

my_var = days_to_units(user_input_number);
print ("#####");
print (my_var);




