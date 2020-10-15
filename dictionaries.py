# define a dictionary data structure

# dictionaries have key:value pairs for the elements
example_dict = {
    "class": "ASTR 119",
    "prof": "Brant",
    "awesomeness": 10
}
print("The type of example_dict is ", type(example_dict))   # Will say <dict>

# get a value via the key
course = example_dict["class"]
print("The course is", course)

# change a value via the key
example_dict["awesomeness"] += 1  # increase awesomeness

# print the dictionary
print(example_dict)

# print dictionary element by element

for x in example_dict.keys():
    print(x, example_dict[x])
