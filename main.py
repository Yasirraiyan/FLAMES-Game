name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Convert names into lists of characters
array1 = list(name1)
array2 = list(name2)

# No need to split again, as they are already lists of characters
first_array = array1
second_array = array2

print("First array is:", first_array)
print("Second array is:", second_array)

# Finding the common elements
common_elements = list(set(first_array) & set(second_array))

# Calculating the length of common elements list
length = len(common_elements)

print("Common elements:", common_elements)
print("Number of common elements:", length)

# Determine the relationship based on the number of common elements
if length == 1:
    print("Friend")
elif length == 2:
    print("Love")
elif length == 3:
    print("Affection")
elif length == 4:
    print("Marriage")
elif length == 5:
    print("Enemy")
elif length == 6:
    print("Siblings")
else:
    print("No specific relationship defined for this number of common elements.")
