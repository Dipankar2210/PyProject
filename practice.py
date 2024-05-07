
# Practice for date time value and general program to calculate value and print output
# from datetime import date
# print(date.today())
# print("Todays date is:" + str(date.today()))

# parsecs_input =  input("Input number of parsecs:")
# print(parsecs_input)
# # parsecs = int(parsecs_input)

# # lightyears = 3.26156 * parsecs

# # print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")


# trying if condition
# a = input("insert first value")
# b = input("insert second value")

# if a < b:
#     print(a)
# elif b<a:
#     print(int(a)+int(b))
# else:
#     print("value of b is", b)

# nested if statement condition and else condition
# a = 16
# b = 25
# c = 27

# if a>b:
#     if b>c:
#         print("a is greater then b and b is greater than c")
#     else:
#         print("a is greater than b and b is less than c")
# elif a == b:
#     print("a is equal to b")
# else:
#     print("a is less than b")

# object_size = 10
# proximity = 5000

# if object_size > 5 and proximity <1000 :
#     print("Evasive maneuvers require")
# else:
#     print("object posses not threat".title())

# print("temperatures and facts about the moon".title())

# some date time work
# from datetime import datetime

# print(datetime.today())

# dt1 = datetime(1983, 10, 22)
# print(dt1)
# print(f'my birtdate is',dt1)

# formated_dt = dt1.strftime("%Y-%m-%d")
# print(formated_dt)

# from datetime import datetime

# # Get the current date and time in various formats
# current_date = datetime.now().date()
# current_time = datetime.now().time()
# current_datetime = datetime.now()

# print("Current date:", current_date)
# print("Current time:", current_time)
# print("Current datetime:", current_datetime)


# from datetime import datetime

# start_time = datetime(2024,4,8,15,30,0)
# end_time = datetime(2024,4,9,10,0,0)

# duration = end_time - start_time
# print(duration.total_seconds())

# # total_seconds = duration.total_seconds()
# # print("Total Seconds",total_seconds)

# from datetime import datetime, timedelta
#
# current_date = datetime.today()
# print(current_date.date())
# # print("current week is",current_date.isocalendar()[1]) *** to get week number
#
# future_date = current_date + timedelta(days=40)
# print(future_date.date())
#
# past_week = current_date - timedelta(weeks=10)
# print(past_week)


