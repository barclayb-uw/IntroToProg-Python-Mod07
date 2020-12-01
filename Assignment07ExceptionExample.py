#---------------------------------------------------------------------
# Title: Assignment 7
# Desc: Script that shows examples of pickling and handling exceptions
# Changelog: (Who, Date, info)
# BBicksler, 11-30-2020, created file, added exception example
#----------------------------------------------------------------------


# This script will ask for two numbers and return the product of them.
print('I will ask for two numbers and give you the product')
# Now I will start a try statement so I make sure numbers are entered
try:
    num1 = int(input('Please enter a number: '))
# If no number is entered exit with this message
except ValueError:
    print('I can only divide with numbers!')
else:
        # I need to do the same for the second number
    try:
        # If no number is entered exit with this message
        num2 = int(input('Please enter a second number: '))
    except ValueError:
        print('I can only divide with numbers!')
    else:
        # Now I need to make sure I am not dividing by 0
        try:
            num1 / num2
        except ZeroDivisionError:
            print('The second number cannot be Zero!')
        else:
            # If everything looks good, do the math!
            print(num1 / num2)
