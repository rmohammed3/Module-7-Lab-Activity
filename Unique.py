# Raheemuddin Mohammed
# August 27, 2025

# Problem 4: Write a Python function that takes a list of numbers and returns a new list
# with unique elements of the first list. Use the append function.

def get_unique_elements(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

# Example usage
original_list = [1, 3, 3, 3, 6, 2, 3, 5]
print(f"Original list: {original_list}")
print(f"Unique list: {get_unique_elements(original_list)}")
