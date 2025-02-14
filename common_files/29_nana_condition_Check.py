#23_jan-2025
user_input_days = input("Enter the number of days\n")
user_input_days_to_int = int(user_input_days)
print(f"Print the user input {user_input_days_to_int}")

total_hours = user_input_days_to_int * 24
#print (f"total hours {total_hours }")

def calculate_hours(days):
    print (days > 0 )
    if ( days > 0 ):
        total_hours = days* 24
        return (f"total hours {total_hours} from function")
    elif ( days == 0 ):
        print("you entered 0 . pls enter valid number  ")
    else:
        print ("you enterered negatie value. so no conversion for you ")

output_of_calculate_hours = calculate_hours(user_input_days_to_int )
print("output_of_calculate_hours")
print(output_of_calculate_hours)

