# Raheemuddin Mohammed
# August 21, 2025
# Description: Function to describe a sandwich with options for filling, bread type, and toasted or not

def make_sandwich(filling, bread="white", toasted=False):
    """Returns a string describing how the sandwich is made"""
    toast_status = "toasted" if toasted else "untoasted"
    return f"Making a {toast_status} {filling} sandwich on a {bread} bread"

# Example call: only with filling and bread
print(make_sandwich("veggie", "rye"))
