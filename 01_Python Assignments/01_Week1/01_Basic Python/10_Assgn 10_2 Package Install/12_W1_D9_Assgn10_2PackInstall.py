'''
***************************************************
Assignment No:10 - Install 2 Package and test it
Day 3 - 10 Days Python Challenge
Assignment Given By: Manoj
***************************************************
'''
# Import external packages
import numpy as np
import requests

# Using numpy (create array and calculate sum)
arr = np.array([10, 20, 30, 40])
print("Array:", arr)
print("Sum of array:", np.sum(arr))

# Using requests (get data from a website)
response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print("Response (first 100 chars):", response.text[:100])