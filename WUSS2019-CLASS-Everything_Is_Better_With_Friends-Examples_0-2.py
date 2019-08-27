# Everything is better with friends:
# Executing SAS® code in Python scripts with SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019
#
# Examples 0-2 Getting Started with Python

# Lines 12 through 19 load necessary modules and define a function to format output.
# Execute without editing

# load all standard library modules needed for examples
import platform


# define utility function to print linebreak-padded output with a title and optional line of 80 stars afterward
def print_with_title(output, title='', linebreaks_before=2, linebreaks_after=2, put_stars_after=True):
    print('\n' * linebreaks_before + title + '\n' * 2, output, '\n' * linebreaks_after, sep='')
    if put_stars_after:
        print('*' * 80)


# Example 0. [Python] Get version number
#
# Uncomment the line of code immediately below, and then execute:

# print_with_title(platform.sys.version, 'Python version being used:')

# Notes:
#
# 1. Assuming a Python 3 kernel is associated with this Notebook, the following should be printed:
#   * the Python version
#   * operating-system information
#
# 2. To increase performance, only a small number of modules in Python's standard library are available by default, so
#    the platform module needs to be explicitly loaded.
#
# 3. This example illustrates three ways Python syntax differs from SAS:
#   * We don't need semicolons at the end of each statement. Unlike SAS, semicolons are optional in Python, and they are
#     typically only used to separate multiple statements placed on the same line (e.g., this example could be written
#     on one line as follows: import platform; print(platform.sys.version)).
#   * The code IMPORT PLATFORM would produce an error. Unlike SAS, capitalization matters in Python.
#   * The platform object module invokes the sub-module object sys nested inside of it, and sys invokes the object
#     version nested inside of it. Unlike SAS, dot-notation has a consistent meaning in Python and can be used to
#     reference objects nested inside each other at any depth. (Think Russian nesting dolls or turduckens.)
#
# 4. If an error is displayed, an incompatible kernel has been chosen. This script was developed using the C-Python
#    3.7.3 kernel as of August 2019.


# Example 1. [Python] Display available modules
#
# Uncomment the lines of code immediately below, and then execute:

# help('modules')
# print_with_title('', linebreaks_before=0, linebreaks_after=0)

# Notes:
#
# 1. All Python modules available to be loaded by the Notebook's kernel should be printed, including
#   * standard library modules (e.g., platform, which was used above),
#   * and any third-party modules that have been installed (e.g., pandas and saspy, which will be used below).
#
# 2. Python has a large standard library because of its "batteries included" philosophy. In addition, numerous
#    third-party modules are actively developed and made freely available through sites like https://github.com/ and
#    https://pypi.org/.
#
# 3. This example illustrates another way Python syntax differs from SAS:
#   * help("modules") would produce identical output. Unlike SAS, single and double quotes always have identical
#     behavior in Python.
# 4. The modules pandas and saspy will need to appear for the remaining examples in this Notebook to work, and saspy
#    will need to be pre-configured to connect to a SAS kernel with access to the sashelp library. Depending on the
#    versions of the modules installed, warnings or errors might also appear.


# Example 2. [Python] Define a str object
#
# Uncomment the lines of code immediately below, and then execute:

# hello_world_str = 'Hello, PyCharm!'
# print_with_title(hello_world_str, 'The value of hello_world_str:')
# if hello_world_str == 'Hello, PyCharm!':
#     print_with_title(type(hello_world_str), 'The type of hello_world_str:')
# else:
#     print_with_title("The string doesn't have the expected value!", 'hello_world_str has been modified:')

# Notes:
#
# 1. A string (str for short) object named hello_world_str is created, and the following are printed:
#   * the value of the string
#   * its type (which is <class 'str'>, reflecting Python primarily being an object-oriented language with class-based
#     inheritance)
#
# 2. This example illustrates three more ways Python syntax differs from SAS:
#   * hello_world_str can be assigned a value virtually anywhere, and it could be reassigned a value later with a
#     completely different type (e.g., hello_world_str = 42 would could type(hello_world_str) to become <class 'int'>).
#     Unlike SAS, variables are dynamically typed in Python.
#   * The code if hello_world_str = 'Hello, PyCharm!' would produce an error. Unlike SAS, single-equals (=) only ever
#     means assignment, and double-equals (==) only ever tests for equality, in Python.
#   * Removing indentation would also produce errors. Unlike SAS, indentation is significant and used to determine scope
#     in Python.
#
# 3. For extra credit, try any or all of the following:
#   * Change the value of hello_world_str when it's created.
#   * Remove the line print(), and look at how the output changes.
#   * Change the value that hello_world_str is compared against in the if-statement.
