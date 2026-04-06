'''
***************************************************
Assignment No:8 - Test all SET Properties
Day 3 - 10 Days Python Challenge
Assignment Given By: Manoj
***************************************************
'''
# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric Difference
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)

# Add an element
set1.add(10)
print("After adding 10 to set1:", set1)

# Remove an element
set1.remove(2)  # Will raise error if 2 not in set
print("After removing 2 from set1:", set1)

# Discard an element (does not raise error)
set1.discard(20)
print("After discarding 20 from set1 (no error if not present):", set1)

# Pop an element (removes random element)
popped_element = set1.pop()
print("Popped element:", popped_element)
print("After pop:", set1)

# Reverse is not applicable for sets (unordered)
# Clear the set
set2.clear()
print("After clearing set2:", set2)

# Convert set to frozenset
frozen_set = frozenset({100, 200, 300})
print("Frozen Set:", frozen_set)

# Using frozenset in a loop
print("Iterating over frozenset:")
for item in frozen_set:
    print(item)