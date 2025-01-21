
to_seconds = 24 * 60 * 60;
name_of_unit = "seconds";

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * to_seconds} {name_of_unit}");
    print("All good");

days_to_units(35)
days_to_units(20)
days_to_units(50)
days_to_units(110)
