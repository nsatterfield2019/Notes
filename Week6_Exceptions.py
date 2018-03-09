# Exceptions

try:
    user_val = int(input("Enter a number:"))
except:
    print("User entered an invalid value")

# Error Types
try:
    int("4")
except ValueError: # improper values or types in a function
    print("Value Error")

# Divide by zero error
try:
    x = 7 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Input Output error
try:
    my_file = open("my_file.txt")
except FileNotFoundError:
    print("file does not exist")
except IOError:
    print("could not open the file")
except:
    print("general exception")

# Identifying errors
try:
    #y = 10 / 0
    int("A")
except Exception as e:
    print(e)

# A better way to ask for input from user
# MPG calculator

val_entered = False

while not val_entered:
    try:
        user_miles = int(input("Enter number of miles:"))
        user_gallons = int(input("Enter number of gallons:"))
        val_entered = True
    except:
        print("User entered an invalid value, try again")

try:
    print("MPG =", user_miles / user_gallons)
except ZeroDivisionError:
    print("Cannot divide by zero")

