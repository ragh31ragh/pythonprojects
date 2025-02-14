from common_files.helper_module_ex_27 import validate_and_execute

user_input=""
while user_input != "exit":
    user_input = input("Hey user, Enter the number of days and conversion unit \n")
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_units_dictionary = {"days":days_and_units[0],"unit":days_and_units[1]}
    print(days_and_units_dictionary)
    validate_and_execute(days_and_units_dictionary)