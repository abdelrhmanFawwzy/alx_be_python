import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    return f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}"


def calculate_future_date():
    current_date = datetime.datetime.now()
    future_date = int(input("Enter the number of days to add to the current date: "))
    time_change = datetime.timedelta(days=future_date)
    future_date  = current_date + time_change
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")


def main():
    current_time = display_current_datetime()
    print(current_time)
    calculate_future_date()
    
if __name__ == "__main__":
     main()