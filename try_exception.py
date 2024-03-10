'''
Python Try Except
The try block lets you test a block of code for errors.
The except block lets you handle the error.
else block lets you execute the code if the try block does not raise any error.
finally block lets you execute the code, regardless of the result of the try- and except blocks.
'''

# Example 1: Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:
try:
  print(x)
except:
    print("An exception occurred")


# Example 2: Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
try:
  print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


# Example 3: Else
    
# You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
  print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Example 4: Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.
# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Raise a TypeError if x is not an integer:
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")



# Next: Assignment