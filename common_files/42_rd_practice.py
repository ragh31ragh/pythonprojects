user_input_days = input("Enter the number of days\n")
user_input_days_to_int = int(user_input_days)
print(f"Print the user input {user_input_days_to_int}")

total_hours = user_input_days_to_int * 24
#print (f"total hours {total_hours }")

def calculate_hours(days):
    total_hours = days* 24
    return (f"total hours {total_hours} from function")

output_of_calculate_hours = calculate_hours(user_input_days_to_int )
print("output_of_calculate_hours")
print(output_of_calculate_hours)

