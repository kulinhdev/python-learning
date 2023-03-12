from contents import pantry

# Create a dictionary
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Access values in the dictionary
print(person['name'])  # prints 'Alice'
print(person['age'])  # prints 25
print(person['city'])  # prints 'New York'

# Add a new key-value pair to the dictionary
person['country'] = 'USA'
print(person)  # prints {'name': 'Alice', 'age': 25, 'city': 'New York', 'country': 'USA'}

# Create a set
s1 = set([1, 2, 3, 4, 5])
s2 = {3, 4, 5, 6, 7}

# Print the sets
print("Set 1", s1)  # prints {1, 2, 3, 4, 5}
print("Set 1", s2)  # prints {3, 4, 5, 6, 7}

# Find the union of the sets
s3 = s1.union(s2)
print("Union 1 & 2", s3)  # prints {1, 2, 3, 4, 5, 6, 7}

# Find the intersection of the sets
s4 = s1.intersection(s2)
print("Intersection 1 & 2", s4)  # prints {3, 4, 5}

# Find the difference of the sets
s5 = s1.difference(s2)
print("Difference 1 via 2", s5)  # prints {1, 2}

