from datetime import datetime

def calculate_age(birth_date):
    # current date and time
    now = datetime.now()

    # Calculate the time difference
    delta = now - birth_date

    # Calculate years, months and days
    years = delta.days // 365
    remaining_days = delta.days % 365
    months = remaining_days // 30
    days = remaining_days % 30

    # Calculate hours, minute and seconds
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    return years, months, days, hours, minutes, seconds

# Input the birth date in the format YYYY-MM-DD
birth_date_input = input("Enter your date of birth (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

# Calculate age
years, months, days, hours, minutes, seconds = calculate_age(birth_date)

# Print the result
print(f"You are {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds old.")
