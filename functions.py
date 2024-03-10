'''
A function is a block of code which only runs when it is called. and it can return data as a result.
'''
USER_NAME = "Sophonie"

# In Python a function is defined using the def keyword
# To call a function, use the function name followed by parenthesis:

#Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.


#Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

def my_first_function():
    print("Hello from my first function")

# This function expects 1 arguments
def my_function(name: str) -> None:
    print(f"Hi, my name is {name}")

def my_function_with_n_parameters(fname: str, lname: str, phone: str) -> str:
    my_var = f"My full names is {fname} {lname}. and my phone numcber is {phone}"
    return my_var

def check_age(name: str,age: int):
    if age < 18:
        print(f"You are not allowed to enter here. Because of your age. {age:}")
    else:
        print(f"Hi {name}. You are welcome in the party")

# Example 5: Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function2(*kids):
  print(f'The youngest child is {kids[2]}')

my_function2("Emil", "Tobias", "Linus")

# Example 6: Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print(f'The youngest child is {child3}')

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# Example 7: Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print(f'His last name is {kid["lname"]}')

my_function(fname = "Tobias", lname = "Refsnes")


# Example 8: Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print(f'I am from {country}')

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Example 9: Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def my_function(food: list):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Example 10: Return Values
# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x


if __name__ == '__main__':
    check_age('Jean', 12)
    check_age(name='Paul', age=20)