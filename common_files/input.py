
to_seconds = 24 * 60 * 60;
name_of_unit = "seconds";

def days_to_units(num_of_days,custom_message):
    print(f"{num_of_days} days are {num_of_days * to_seconds} {name_of_unit}");
    print("All good");

days_to_units(35,"This is 1")
days_to_units(20,"Good")
days_to_units(50,"Third")
days_to_units(110,"very good")

def scope_check():
    print(name_of_unit)

user_input = input("Enter number of days:\n");
print("########");
print(user_input);





