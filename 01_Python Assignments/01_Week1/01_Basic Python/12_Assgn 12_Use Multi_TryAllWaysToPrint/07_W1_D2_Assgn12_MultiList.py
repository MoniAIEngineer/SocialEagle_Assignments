'''
*************************************************************
Assignment No:12 - Try Multiple Lists and print their ouput
1. First Sub-List
2. Deeply Nested (Multi-Level)
3. Mixed Data Types
4. Loop Through Nested List
5. Flatten Nested List (1 Level)
6. List Multiplication (Important Case)
7. Modify Nested Elements
8. Add Elements
9. Remove Elements
10. 3D List (Multiple Levels)
11. Traverse 3D List
12. List Comprehension (Nested)
13. Check Type and Length
Day 2 - 10 Days Python Challenge
Assignment Given By: Manoj
************************************************************
'''
# ================================
# NESTED MULTI-LEVEL LIST PRACTICE
# ================================

print("=== 1. Basic Nested List ===")
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Full list:", nested)
print("First sublist:", nested[0])
print("Element (row 1, col 2):", nested[0][1])  # 2
print("Element (row 1, col 2):", nested[0][2]) 
print("Element (row 1, col 2):", nested[1][2]) 

print("\n=== 2. Deeply Nested (Multi-Level) ===")
deep = [1, [2, [3, [4, [5]]]]]
print("Full structure:", deep)
print("Access 5:", deep[1][1][1][1][0])

print("\n=== 3. Mixed Data Types ===")
mixed = [1, "hello", [3.5, True, ["deep", 99]]]
print("Full list:", mixed)
print("Access 'deep':", mixed[2][2][0])

print("\n=== 4. Loop Through Nested List ===")
for i, sublist in enumerate(nested):
    for j, value in enumerate(sublist):
        print(f"Position [{i}][{j}] = {value}")

print("\n=== 5. Flatten Nested List (1 Level) ===")
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)
print("Flattened:", flat)

print("\n=== 6. List Multiplication (Important Case) ===")
bad = [[0] * 3] * 3
print("Before change:", bad)
bad[0][0] = 99
print("After change (unexpected!):", bad)

print("\nCorrect way:")
good = [[0 for _ in range(3)] for _ in range(3)]
good[0][0] = 99
print("Correct result:", good)

print("\n=== 7. Modify Nested Elements ===")
nested[1][1] = 55
print("Updated list:", nested)

print("\n=== 8. Add Elements ===")
nested.append([10, 11, 12])
print("After append:", nested)

nested[0].append(100)
print("Add inside sublist:", nested)

print("\n=== 9. Remove Elements ===")
nested.pop()  # remove last sublist
print("After removing last sublist:", nested)

nested[0].remove(100)
print("After removing 100:", nested)

print("\n=== 10. 3D List (Multiple Levels) ===")
three_d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
print("3D list:", three_d)
print("Access 6:", three_d[1][0][1])

print("\n=== 11. Traverse 3D List ===")
for i in range(len(three_d)):
    for j in range(len(three_d[i])):
        for k in range(len(three_d[i][j])):
            print(f"[{i}][{j}][{k}] = {three_d[i][j][k]}")

print("\n=== 12. List Comprehension (Nested) ===")
matrix = [[i * j for j in range(3)] for i in range(3)]
print("Matrix:", matrix)

print("\n=== 13. Check Type and Length ===")
print("Type:", type(nested))
print("Length:", len(nested))
print("Length of first sublist:", len(nested[0]))

print("\n=== DONE ===")