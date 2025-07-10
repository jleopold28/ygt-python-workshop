# Example 1: Add numbers
# Create a function to add 2 integers
def add_numbers(int1, int2):
    sum = int1 + int2
    # Remember to return the value in the function
    return sum

new_value = add_numbers(5, 10)
print(new_value)

new_value = add_numbers(23, 166)
print(new_value)

# Example 2: Calculate Grade

def final_grade(score_list):
    # calculate the total points scored
    # NOTE: sum is built-in function in python which can add all values in a list
    my_points = sum(score_list)

    # find max points. Should be the number of assignments multiplied by 100
    # NOTE: len is a built-int function in python to tell you how many items are in a list
    max_points = len(score_list) * 100

    # Get a percent score
    percent_score = my_points / max_points
    
    # multiply by 100 to convert percentage to value
    grade = percent_score * 100

    return grade

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
# define the scores
my_scores = [84, 31, 89, 90, 75, 66, 77, 85]

# call our function with the list input
my_grade = final_grade(my_scores)
letter = letter_grade(my_grade)

# print the result
print(f"My final grade was {my_grade} or {letter}")

