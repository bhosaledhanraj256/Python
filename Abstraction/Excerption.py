try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid number!")
else:
    print("Division successful! Result =", result)
finally:
    print("This will always run (cleanup, closing files, etc.)")
