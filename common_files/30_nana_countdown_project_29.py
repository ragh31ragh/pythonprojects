import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
#python:10:2:2021
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

print(input_list)

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()

print(deadline_date - today_date)
