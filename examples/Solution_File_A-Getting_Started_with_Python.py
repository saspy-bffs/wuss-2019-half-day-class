# Everything is better with friends: Executing SAS® code in Python scripts with
# SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019


###############################################################################
# Exercises 0-2: Getting Started with Python                                  #
###############################################################################

# Lines 12-13 load modules needed for exercises and should be left as-is
from class_setup import print_with_title
import platform




###############################################################################
#                                                                             #
# Exercise 0. [Python] Get version number                                     #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


print_with_title(platform.sys.version, 'Python version being used:')


# Notes:
#
# 1. The following should be printed:
#    * Python version information
#    * Operating System information
#
# 2. To increase performance, only a small number of modules in Python's
#    standard library are available by default, so the platform module was
#    explicitly loaded at the start of this file.
#
# 3. This example illustrates three ways Python syntax differs from SAS:
#    * We don't need semicolons at the end of each statement. Unlike SAS,
#      semicolons are optional in Python, and they are typically only used to
#      separate multiple statements placed on the same line.
#    * The code PLATFORM.SYS.VERSION would produce an error. Unlike SAS,
#      capitalization matters in Python.
#    * The platform object module invokes the sub-module object sys nested
#      inside of it, and sys invokes the object version nested inside of it.
#      Unlike SAS, dot-notation has a consistent meaning in Python and can be
#      used to reference objects nested inside each other at any depth. (Think
#      Russian nesting dolls or turduckens.)




###############################################################################
#                                                                             #
# Exercise 1. [Python] Display available modules                              #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


help('modules')
print_with_title('', linebreaks_before=0, linebreaks_after=0)


# Notes:
#
# 1. All Python modules available should be printed, including the following:
#    * standard library modules (e.g., platform, which was used above)
#    * any third-party modules that have been installed (e.g., pandas and
#    saspy, which should appear if the requirements.txt file is satisfied)
#
# 2. Python has a large standard library because of its "batteries included"
#    philosophy. In addition, numerous third-party modules are actively
#    developed and made freely available through sites like https://github.com/
#    and https://pypi.org/.
#
# 3. This example illustrates another way Python syntax differs from SAS:
#    * help("modules") is interchangeable with help('modules'). Unlike SAS,
#      single and double quotes always have identical behavior in Python.
#
# 4. Depending on the versions of the modules installed, warnings or errors
#    might appear.




###############################################################################
#                                                                             #
# Exercise 2. [Python] Define a str object                                    #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# Original version
hello_world_str = 'Hello, PyCharm!'
print_with_title(hello_world_str, 'The value of hello_world_str:')
if hello_world_str == 'Hello, PyCharm!':
    print_with_title(type(hello_world_str), 'The type of hello_world_str:')
else:
    print_with_title(
        "The string doesn't have the expected value!",
        'hello_world_str has been modified:'
    )

# Change the value of hello_world_str to a number and then find its type.
hello_world_str = 42
print(f"If hello_world_str = 42, then it's type is {type(hello_world_str)}.")

# Change the value of hello_world_str when it's created
hello_world_str = 'Hello, PyCharm Community Edition!'
print_with_title(hello_world_str, 'The value of hello_world_str:')
if hello_world_str == 'Hello, PyCharm!':
    print_with_title(type(hello_world_str), 'The type of hello_world_str:')
else:
    print_with_title(
        "The string doesn't have the expected value!",
        'hello_world_str has been modified:'
    )

# Change the value that hello_world_str is compared against in the if-statement
hello_world_str = 'Hello, PyCharm!'
print_with_title(hello_world_str, 'The value of hello_world_str:')
if hello_world_str == 'Hello, PyCharm Community Edition!':
    print_with_title(type(hello_world_str), 'The type of hello_world_str:')
else:
    print_with_title(
        "The string doesn't have the expected value!",
        'hello_world_str has been modified:'
    )


# Notes:
#
# 1. A string (str for short) object named hello_world_str is created, and the
#    following are printed:
#    * the value of the string
#    * its type (which is <class 'str'>, reflecting Python primarily being an
#      object-oriented language with class-based inheritance)
#
# 2. This illustrates three more ways Python syntax differs from SAS:
#    * hello_world_str can be assigned a value virtually anywhere, and it could
#      be reassigned a value later with a completely different type. Unlike
#      SAS, variables are dynamically typed in Python.
#    * The code
#          if hello_world_str = 'Hello, PyCharm!'
#      would produce an error. Unlike SAS, single-equals (=) only ever means
#      assignment, and double-equals (==) only ever tests for equality, in
#      Python.
#    * Removing indentation would also produce errors. Unlike SAS, indentation
#      is significant and used to determine scope in Python.
#
# 3. For additional practice, try any or all of the following:
#    * Change the value of hello_world_str to a number (e.g., 42), and then
#      find its type.
#    * Change the value of hello_world_str when it's created.
#    * Change the value that hello_world_str is compared against in the
#      if-statement.
