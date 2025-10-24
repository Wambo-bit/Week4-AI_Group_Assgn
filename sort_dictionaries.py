#Write a function to sort a list of dictionaries by a specific key
def sort_dicts_ai(data, sort_key, reverse=False):
    """
    Sorts a list of dictionaries by a specific key.

    Parameters:
    data (list): A list of dictionaries to be sorted.
    sort_key (str): The key in the dictionaries to sort by.
    reverse (bool): If True, sort in descending order. Default is False (ascending order).

    Returns:
    list: A new list of dictionaries sorted by the specified key.
    """
    try:
        sorted_data = sorted(data, key=lambda x: x[sort_key], reverse=reverse)
        return sorted_data
    except KeyError as e:
        print(f"KeyError: One or more dictionaries do not contain the key '{sort_key}'. {e}")
        return []
    except TypeError as e:
        print(f"TypeError: Cannot sort due to incompatible types. {e}")
        return []
# Example usage:
if __name__ == "__main__":
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    sorted_by_age = sort_dicts_ai(sample_data, 'age')
    print("Sorted by age (ascending):", sorted_by_age)
    
    sorted_by_name_desc = sort_dicts_ai(sample_data, 'name', reverse=True)
    print("Sorted by name (descending):", sorted_by_name_desc)

#MANUAL CODE:
# Function: sort_by_key
# Purpose: Sorts a list of dictionaries based on a key you choose
# Example:
#   Input: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
#   sort_by_key(data, 'age') → [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]

def sort_by_key(data, key):
    """
    Sort a list of dictionaries by a specific key.
    
    Parameters:
    data (list): A list of dictionaries to be sorted.
    key (str): The key to sort the dictionaries by.
    
    Returns:
    list: A new sorted list of dictionaries.
    """
    # The sorted() function sorts items.
    # key=lambda x: x[key] means "use the value of x[key] for sorting".
    # For example, if key='age', it sorts using each person's age.
    return sorted(data, key=lambda x: x[key])


# Example usage:
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Charlie', 'age': 30},
    {'name': 'Bob', 'age': 20}
]

# We sort by the key 'age'
sorted_people = sort_by_key(people, 'age')
print(sorted_people)


