# Simple Password Validator

# Ask the user for a password
password = input("Enter a password: ")
 
# Check the password length
if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    # Check if the password contains both letters and numbers
    has_letter = False
    has_number = False
 
    for char in password:
        if char.isalpha():  # Check if the character is a letter
            has_letter = True
        elif char.isdigit():  # Check if the character is a number
            has_number = True
 
    if has_letter and has_number:
        print("Password is valid.")
    else:
        print("Password must contain both letters and numbers.")
