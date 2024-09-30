from datetime import datetime
def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date
integer = input("Enter the number of days to add to the current date: ")
def calculate_future_date():
    future_date = datetime.datetime.now()+datetime.timedelta(days = int(integer))
    return future_date.strftime("%Y-%m-%d %H:%M:%S")

print("Current date and time: ",display_current_datetime())
print("future date: ",calculate_future_date())
