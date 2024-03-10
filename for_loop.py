'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
'''


cars = ["Ford", "V8", "Lambo","Volvo", "BMW"]
colors = ['red', 'blue', 'orange']

for x in cars:
  print(x)

# Example 2: Iterating through a string
for x in "banana":
  print(x)

# Example 3: The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)
  if x == "Volvo":
    break
  
# The for loop does not require an indexing variable to set beforehand.
  
# Example 4: The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  if x == "Volvo":
    continue
  print(x)


# Example 5: The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
  
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)

# Example 6: Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
    print("Finally finished!")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.
    
# Example 7: Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


