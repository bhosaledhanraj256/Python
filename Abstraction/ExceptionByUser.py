# Step 1: Create a custom exception class
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above!")
    else:
        print("You are eligible to vote.")

except InvalidAgeError as e:
    print("Custom Exception Caught:", e)

except ValueError:
    print("Please enter a valid number!")

else:
    print("No exception occurred.")

finally:
    print("Program finished.")
