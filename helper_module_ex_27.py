

def days_to_units(number_of_days,conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are { number_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 *60 } minutes"
    else:
        return "unsupported unit"

def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        if user_input_number > 0 :
            calculated_value = days_to_units(user_input_number,days_and_units_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0 , please enter valid number ")
        else:
            print(" you entered negative number - no conversion for you ")
    except:
        print("In exception BLOCK")


