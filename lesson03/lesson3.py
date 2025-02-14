# Lesson 3
tiles = input("Enter number of tiles: ")
#imput always a string
tiles = int(tiles)

# Square root is just the exponent of a half
calculation = int((tiles ** 0.5) // 1)

print(f"The maximum sidelenght is:  {calculation}")
# or 
# import math 
# calculations = math.sqrt(tiles)

print (f"Number of tiles: {tiles}")
