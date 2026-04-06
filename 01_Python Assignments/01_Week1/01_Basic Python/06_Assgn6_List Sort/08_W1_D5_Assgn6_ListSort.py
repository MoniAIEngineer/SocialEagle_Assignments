'''
***************************************************
Assignment No:6 - Try all Lists Functions till Sort
Day 3 - 10 Days Python Challenge
Assignment Given By: Manoj
***************************************************
'''
# List of tasks
Task = ['Eat', 'Code', 'Sleep']

# Print original list
print("Original list:", Task)

# Append a new item
Task.append('Exercise')
print("After append:", Task)

# Copy the list
Task_copy = Task.copy()
print("Copied list:", Task_copy)

# Count how many times 'Code' appears
code_count = Task.count('Code')
print("Count of 'Code':", code_count)

# Extend the list with another list
Task.extend(['Read', 'Play'])
print("After extend:", Task)

# Find the index of 'Sleep'
sleep_index = Task.index('Sleep')
print("Index of 'Sleep':", sleep_index)

# Insert 'Meditate' at position 1
Task.insert(1, 'Meditate')
print("After insert:", Task)

# Pop the last item
popped_item = Task.pop()
print("Popped item:", popped_item)
print("After pop:", Task)

# Remove 'Eat' from the list
Task.remove('Eat')
print("After remove:", Task)

# Reverse the list
Task.reverse()
print("After reverse:", Task)

# Sort the list alphabetically
Task.sort()
print("After sort:", Task)