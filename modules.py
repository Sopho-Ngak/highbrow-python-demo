'''
What is a module?
A file containing a set of functions you want to include in your application.

package
library

sudo apt-get install python3-pip

pip install name_of_the_package
pip uninstall name_of_the_package

pip
'''
# Example 1: Create a Module
# To create a module just save the code you want in a file with the file extension .py:

# from functions import my_first_function, my_function_with_n_parameters, USER_NAME
# import functions

# What is PIP?
# PIP is a package manager for Python packages
# You can use pip to install packages from the Python Package Index and other indexes.
# Libraries are a collection of functions and methods that allows you to perform many actions without writing your code.
# check if pip is installed
# pip --version
# If not install in ubuntu with this command
# sudo apt install python3-pip
# To instal a package use this command
# pip install camelcase

# Remove a Package
# Use the uninstall command to remove a package:
# pip uninstall camelcase

# List Packages
# Use the list command to list all the packages installed on your system:
# pip list

# Python virtual environment on ubuntu
# sudo apt install python3-venv
# python3 -m venv myenv
# source myenv/bin/activate

from functions import *




if __name__ == '__main__':
    my_first_function()
    response = my_function_with_n_parameters(fname='Jules', lname='Tosin', phone='+12345678')
    print(USER_NAME)