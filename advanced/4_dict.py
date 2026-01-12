# Create a dictionary
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'DOB': '1993-01-15'
}

# Accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict.get('age'))

# Adding a new key-value pair
my_dict['profession'] = 'Engineer'
print("Updated Dictionary:", my_dict)

# Modifying an existing value
my_dict['city'] = 'San Francisco'
print("Modified Dictionary:", my_dict)

# Using pop to remove a key-value pair and return the value
my_dict.pop('age')
print("After Popping Age:", my_dict)