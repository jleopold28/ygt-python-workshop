# Example 1: Lists with for loop
my_friends = ["Greg", "Laura", "Tim"]

for person in my_friends:
    print(f"Hello {person}!")

# Example 2: Lists with while loop

index = 0
while index < len(my_friends):
    print(f"Hello {my_friends[index]}!")
    index = index + 1