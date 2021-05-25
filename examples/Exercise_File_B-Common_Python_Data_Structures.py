# Everything is better with friends: Executing SAS® code in Python scripts with
# SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019


###############################################################################
# Exercises 3-5: Common Python Data Structures                                #
###############################################################################

# Lines 12-13 load modules needed for exercises and should be left as-is
from class_setup import print_with_title
from pandas import DataFrame




###############################################################################
#                                                                             #
# Exercise 3. [Python] Define a list object                                   #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# hello_world_list = ['Hello', 'list']
# print_with_title(hello_world_list, 'The value of hello_world_list:')
# print_with_title(type(hello_world_list), 'The type of hello_world_list:')


# Notes:
#
# 1. A list object named hello_world_list with two values is created, and the
#    following are printed:
#    * the value of the list
#    * its type (which is <class 'list'>)
#
# 2. Lists are the most fundamental Python data structure and are related to
#    SAS data-step arrays. Values in lists are always kept in insertion order,
#    meaning the order they appear in the list's definition, and they can be
#    individually accessed using numerical indexes within bracket notation:
#    * hello_world_list[0] returns 'Hello'
#    * hello_world_list[1] returns 'list'
#
# 3. This example illustrates another way Python syntax differs from SAS:
#    * The left-most element of a list is always at index 0. Unlike SAS,
#      customized indexing is only available for more sophisticated data
#      structures in Python (e.g., a dictionary, as in the next example).
#
# 4. For additional practice, try any or all of the following:
#    * Print out the initial element of the list.
#    * Print out the final element of the list.
#    * Create a list of length five, and print its middle elements.




###############################################################################
#                                                                             #
# Exercise 4. [Python] Define a dict object                                   #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# hello_world_dict = {
#     'salutation'      : ['Hello'       , 'dict'],
#     'valediction'     : ['Goodbye'     , 'list'],
#     'part of speech'  : ['interjection', 'noun'],
# }
# print_with_title(hello_world_dict, 'The value of hello_world_dict:')
# print_with_title(type(hello_world_dict), 'The type of hello_world_dict:')


# Notes:
# 1. A dictionary (dict for short) object named hello_world_dict with three
#    key-value pairs is created, and the following are printed:
#    * the value of the dictionary
#    * its type (which is <class 'dict'>)
#
# 2. Dictionaries are another fundamental Python data structure and are related
#    to SAS formats and data-step hash tables. Dictionaries are more generally
#    called associative arrays or maps because they map keys (appearing before
#    the colons) to values (appearing after the colons). In other words, the
#    value associated with each key can be accessed using bracket notation:
#    * hello_world_dict['salutation'] returns ['Hello', 'dict']
#    * hello_world_dict['valediction'] returns ['Goodbye', 'list']
#    * hello_world_dict['part of speech'] returns ['interjection', 'noun']
#
# 3. Whenever indexable data structures are nested in Python, indexing methods
#    can be combined. E.g., hello_world_dict['salutation'][0] is the same as
#    ['Hello', 'dict'][0], which returns 'Hello'.
#
# 4. When using older versions of Python, the print order of key-value pairs
#    may not match insertion order, meaning the order key-value pairs are
#    listed when the dictionary is created. However, as of Python 3.7 (released
#    in June 2018), insertion order is preserved.
#
# 5. For additional practice, try any or all of the following:
#    * Print out the list with key 'salutation'.
#    * Print out the initial element in the list associated with key
#      'valediction'.
#    * Print out the final element in the list associated with key 'part of
#      speech'.




###############################################################################
#                                                                             #
# Exercise 5. [Python w/ pandas] Define a DataFrame object                    #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# hello_world_df = DataFrame(
#     {
#         'salutation':     ['Hello'      , 'DataFrame'],
#         'valediction':    ['Goodbye'    , 'dict'],
#         'part of speech': ['exclamation', 'noun'],
#     }
# )
# print_with_title(hello_world_df, 'The value of hello_world_df:')
# print_with_title(hello_world_df.shape, 'The shape of hello_world_df:')
# hello_world_df.info()
# print_with_title('', linebreaks_before=0, linebreaks_after=0)


# Notes:
#
# 1. A DataFrame (df for short) object named hello_world_df with dimensions 2x3
#    (2 rows by 3 columns) is created, and the following are printed:
#    * the value of the DataFrame
#    * the number of rows and columns in hello_world_df
#    * some information about it, which is obtained by hello_world_df calling
#      its info method (meaning a function whose definition is nested in it)
#
# 2. Since DataFrames are not built into Python, we had to import their
#    definition from the pandas module at the beginning of this file. Like
#    their R counterpart, DataFrames are two-dimensional arrays of values that
#    can be thought of like SAS datasets. However, while SAS datasets are
#    typically only accessed from disk and processed row-by-row, DataFrames are
#    loaded into memory all at once. This means values in DataFrames can be
#    randomly accessed, but it also means the size of DataFrames can't grow
#    beyond available memory.
#
# 3. The dimensions of the DataFrame are determined as follows:
#    * The keys 'salutation', 'valediction', and 'part of speech' of the
#      dictionary passed to the DataFrame constructor function become column
#      labels.
#    * Because each key maps to a list of length two, each column will be two
#      elements tall (with an error occurring if the lists are not of
#      non-uniform length).
#
# 4. This example gives one option for building a DataFrame, but the
#    constructor function can also accept many other object types, including
#    another DataFrame.
#
# 5. For additional practice, try any or all of the following (keeping in mind
#    that DataFrames can be indexed like dictionaries):
#    * Print out the column with key 'salutation'.
#    * Print out the initial element in the column with key 'valediction'.
#    * Print out the final element in the column with key 'part of speech'.
