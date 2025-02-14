#23_jan-2025
#user_input_days = input("Enter the number of days\n")
#user_input_days_to_int = int(user_input_days)
#print(f"Print the user input {user_input_days_to_int}")

#total_hours = user_input_days_to_int * 24
#print (f"total hours {total_hours }")

def calculate_hours(days):
    total_hours = days * 24
    return (f"total hours {total_hours} from function")



def validate_and_execute():
    try:
        print("In try block")
        user_input_days_int = int(number_of_days_element);
        print("user_input_days_int=")
        print(user_input_days_int)
        if (user_input_days_int > 0 ):
            total_hours = user_input_days_int * 24
            print(f"total hours {total_hours} from function")
        elif (user_input_days_int == 0):
            print("you entered 0 . pls enter valid number  ")
    except :
        print("In except block")
        print("your input is not a number ")

user_input_days = ""
while user_input_days != "exit":
    user_input_days = input("1.Enter the number of days in csv, and i will provide you hours \n")
    print(type(user_input_days.split(",")))
    print(user_input_days.split(","))
    for number_of_days_element in user_input_days.split(","):
        validate_and_execute()
