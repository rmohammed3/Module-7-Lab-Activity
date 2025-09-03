# Raheemuddin Mohammed
# August 27, 2025

# Problem 3: Write a Python function to multiply all the numbers in a list.
# Use list [5, 2, 7, -1].

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
nums = [5, 2, 7, -1]
print(f"The product of the list {nums} is {multiply_list(nums)}")
