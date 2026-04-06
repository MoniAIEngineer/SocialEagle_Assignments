'''
***************************************************
Assignment No:7 - Merge 2 Dictionary into 1
Day 3 - 10 Days Python Challenge
Assignment Given By: Manoj
***************************************************
'''
# Create three dictionaries
dict1 = {'Name': 'Alice', 'Age': 25}
dict2 = {'City': 'New York', 'Country': 'USA'}
dict3 = {'Hobby': 'Reading', 'Profession': 'Engineer'}

# Print the original dictionaries
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)

# Merge all three dictionaries into one
merged_dict = {**dict1, **dict2, **dict3}

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)