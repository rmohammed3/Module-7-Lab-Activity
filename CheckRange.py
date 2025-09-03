# Raheemuddin Mohammed
# August 27, 2025

# Problem 2: Write a Python function to check whether a number is in a given range.
# Use range(1,10). Print whether the number is in or not in the range.

def check_range(num):
    if num in range(1, 10):
        print(f"{num} is in the range.")
    else:
        print(f"{num} is not in the range.")

# Example usage
check_range(5)
check_range(12)
