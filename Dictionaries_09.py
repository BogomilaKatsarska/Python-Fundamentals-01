# Unordered collection
# Keys must be of immutable type and must be unique
# my_dict has 2 elements
my_dict = {"fruit": "apple", "vegetable": "cucumber"}
print(my_dict["fruit"])
print(my_dict.get('orange'))
print(my_dict.get('cat', 'unknown word for this dict'))
# Dictionaries are mutable collection - we can add new items or change the value of the existing one
my_dict["fruit"] = "banana"
print(my_dict)
my_dict["other"] = "sth_new"
print(my_dict)
my_dict.update({'dog': 'kuche'})
print(my_dict)
my_dict.update({'dog': 'bau_bau'})
print(my_dict)

squares = {1: 1, 2:4, 3:9}

for key in squares.keys():
    squares[key]**=2
print(squares)

numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
for key in numbers:
    print(key, numbers[key])

for key, value in numbers.items():
    print(key, value)