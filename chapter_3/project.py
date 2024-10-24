# Simple Age Calculator

# Ask the user for their birth year
birth_year = input("What year were you born? ")
 
# Convert the input to an integer
birth_year = int(birth_year)
 
# Calculate the current age
current_year = 2024
age = current_year - birth_year
 
# Print the result
print(f"You are {age} years old.")
