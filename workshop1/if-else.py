# Example 1: IF/ELSE
temp = 102

if temp > 90:
    print(f"It's hot out! The temp is {temp} degrees")
else:
    print(f"It's cold out! The temp is {temp} degrees")

# Example 2: Add Elif

temperature = 80

if temperature > 100:
    print("It's hot out")
    print("Make sure to stay hydrated!")
    # Remember that indentation represents a BLOCK of code
elif temperature > 65: # value is between 65 and 100
    print("It's a nice day!")
elif temperature > 40: # value is between 40 and 60
    print("It's a bit cold out")
else: # value is below 40
    print("It's freezing!")

# Example 3: And/Or Weather

temp = 40
is_sunny = False

if temp > 50 and is_sunny:
    print("It's a nice day!")
elif temp > 50 and not is_sunny:
    print("It's a bit dreary out")
elif temp < 50 and is_sunny:
    print("It's dry and cold out")
elif temp < 50 and not is_sunny:
    print("It's a gross day")
else:
    print("It's something else...")

# Example 4: And/Or Discount
is_vet = False
age = 70

if is_vet or age >= 65:
    print("You get a discount!")
else:
    print("Sorry, no discount.")

# Example 5: Truth Tables - OR vs AND
age = 29
is_student = False

if age < 30 or is_student:
    print("Your age is under 30 OR you are a student, possibly both!")

if age < 30 and is_student:
    print("Your age is under 30 AND you are a student!")


