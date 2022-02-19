# Checking human life in weeks
#
age = input("Please enter your age : ")
#
# Checking the remaining weeks and years nd months

remaining_years = 90 - int(age)
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365
remaining_months = remaining_years * 12
print(f"Your remaining age is : {remaining_years}")
print(f"Your remaining days is : {remaining_days}")
print(f"Your remaining weeks is : {remaining_weeks}")
print(f"Your remaining months is : {remaining_months}")
#
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left")