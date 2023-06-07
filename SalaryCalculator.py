#This program prompts the user to enter the number of hours worked and the hourly rate.
#With that information, it calculates the corresponding salary, taking into account that hours exceeding a total of 40 worked hours will be paid at a rate equivalent to one and a half hours.

while True:
    hours = input('Enter the number of hours worked: ')
    try:
        hours = float(hours)
        break  # Continue if a valid number has been entered
    except ValueError:
        print('Error, please enter a valid number')

while True:
    rate = input('Enter the hourly rate: ')
    try:
        rate = float(rate)
        break  # Continue if a valid number has been entered
    except ValueError:
        print('Error, please enter a valid number')

if hours > 40.0:
    overtime_hours = hours - 40.0
    overtime_rate = rate * 1.5
    salary = ((hours - overtime_hours) * rate) + (overtime_hours * overtime_rate)
else:
    salary = hours * rate

print('Salary:', salary)

#In this code, a while loop is used to repeatedly prompt for input until a valid numeric value is entered.
#If a non-numeric value is entered, an error message is displayed and the input is requested again.
#The loop will continue until a valid value is entered, at which point the loop will be broken and the program will continue executing.
