def is_leap(year):

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# prompt the user to enter a year
year_str = input("Enter a year: ")

# check if the year is a valid 4-digit number
if not year_str.isdigit() or len(year_str) != 4:
    print("Error: Please enter a valid 4-digit for a year .")
else:
    # convert the year to an integer and check if it's a leap year
    year = int(year_str)
    if is_leap(year):
        print("true " + f"{year} is a leap year.")
    else:
        print("false " + f"{year} is not a leap year.")