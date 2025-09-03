# Raheemuddin Mohammed
# August 21, 2025
# CSS 225 - Week 07 Assignment


# PART 1: WITHOUT USING FUNCTIONS
# Person 1
name1 = "Alice"
age1 = 25
print("Hello", name1 + "!")
print("You are", age1 * 12, "months old.")

# Person 2
name2 = "Bob"
age2 = 30
print("Hello", name2 + "!")
print("You are", age2 * 12, "months old.")

# Person 3
name3 = "Charlie"
age3 = 22
print("Hello", name3 + "!")
print("You are", age3 * 12, "months old.")


# PART 2: USING FUNCTION

def greet_and_calculate_age(name, years):
    print("Hello", name + "!")
    return years * 12

# Function calls
months1 = greet_and_calculate_age("Alice", 25)
print("You are", months1, "months old.")

months2 = greet_and_calculate_age("Bob", 30)
print("You are", months2, "months old.")

months3 = greet_and_calculate_age("Charlie", 22)
print("You are", months3, "months old.")
