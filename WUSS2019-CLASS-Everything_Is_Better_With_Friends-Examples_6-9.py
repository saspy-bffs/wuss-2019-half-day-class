# Everything is better with friends:
# Executing SAS® code in Python scripts with SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019
#
# Examples 6-9 Common Python Data Structures

# Lines 12 through 20 load necessary modules and define a function to format output.
# Execute without editing

# load all third-party modules needed for examples
from pandas import DataFrame
from saspy import SASsession


# define utility function to print linebreak-padded output with a title and optional line of 80 stars afterward
def print_with_title(output, title='', linebreaks_before=2, linebreaks_after=2, put_stars_after=True):
    print('\n' * linebreaks_before + title + '\n' * 2, output, '\n' * linebreaks_after, sep='')
    if put_stars_after:
        print('*' * 80)


# Example 6. [Python w/ saspy] Connect to a SAS kernel
#
# Uncomment the lines of code immediately below, and then execute:

# sas = SASsession()
# print_with_title(type(sas), 'The type of SAS session object sas:')

# Notes:
#
# 1. A SASsession object named sas is created, and the following are printed:
#   * confirmation a SAS session has been established
#   * the type of object sas (which is saspy.sasbase.SASsession)
#
# 2. As with the DataFrame object type above, SASsession is not built into Python, so we first need to import its
#    definition from the saspy module.
#
# 3. The code from saspy import SASsession; sas = SASsession() only needs to be used to establish a SAS kernel
#    connection once within a given Python session. All subsequent cells in this Notebook will assume these lines have
#    been executed.

# Example 7. [Python w/ pandas & saspy] Load a SAS dataset into a DataFrame
#
# Uncomment the lines of code immediately below, and then execute:

# fish_df = sas.sasdata2dataframe(table='fish', libref='sashelp')
# print_with_title(fish_df, 'The value of fish_df:')
# print_with_title(fish_df.describe(), 'The Python equivalent of PROC MEANS using fish_df:')
# print_with_title(fish_df.head(), 'The first five rows of fish_df:')

# Notes:
#
# 1. A DataFrame object named fish_df with dimensions 159x7 (159 rows and 7 columns) is created from the SAS dataset
#    fish in the sashelp library, and the following are printed with blank lines between them:
#   * the type of object fish_df (which is <class 'pandas.core.frame.DataFrame'>)
#   * the first five rows of fish_df, which are at row indices 0 through 4 since Python uses zero-based indexing
#   * summary information about its 6 numerical columns, which is obtained by fish_df calling its describe method (the
#     pandas equivalent of the SAS MEANS procedure)
#
# 2. The sas object represents a connection to a SAS session and was created when a previous cell was run. Here, sas
#    calls its sasdata2dataframe method to access the SAS library sashelp defined within this SAS session and to load
#    the entire contents of SAS dataset sashelp.fish into the DataFrame fish_df.
#
# 3. For extra credit, try the following:
#   * Pass a numerical parameter to the head method to see a different number of rows (e.g., fish_df.head(42)).
#   * Change the head method to tail to see a different part of the dataset.
#   * To view other portions of fish_df, explore the more advanced indexing methods loc and iloc explained at
#     https://brohrer.github.io/dataframe_indexing.html.


# Example 8. [Python w/ pandas] Manipulate a DataFrame
#
# Uncomment the lines of code immediately below, and then execute:

# fish_df_g   = fish_df.groupby('Species')
# fish_df_gs  = fish_df_g['Weight']
# fish_df_gsa = fish_df_gs.agg(['count', 'std', 'mean', 'min', 'max'])
# print_with_title(fish_df_gsa, 'The Python equivalent of PROC MEANS with CLASS and VAR statements:')

# Notes:
#
# 1. The DataFrame fish_df, which was created in a cell above from the SAS dataset sashelp.fish, is manipulated, and the
#    following is printed:
#   * a table giving the number of rows, standard deviation, mean, min, and max of Weight in fish_df when aggregated by
#     Species
#
# 2. This is accomplished by creating a series of new DataFrames:
#   * The DataFrame fish_df_g is created from fish_df using the groupby method to group rows by values in column
#     'Species'.
#   * The DataFrame fish_df_gs is created from fish_df_g by extracting the 'Weight' column using bracket notation.
#   * The DataFrame fish_df_gsa is created from fish_df_gs using the agg method to aggregate by the functions in the
#     list ['count', 'std', 'mean', 'min', 'max'].
#
# 3. Identical results could be obtained using the following SAS code:
#        proc means data=sashelp.fish std mean min max;
#             class species;
#             var Weight;
#        run;
#    However, while PROC MEANS operates on SAS datasets row-by-row from disk, DataFrames are stored entirely in main
#    memory. This allows any number of DataFrame operations to be combined for on-the-fly reshaping using "method
#    chaining." In other words, fish_df_gsa could have instead been created with the following one-liner, which avoids
#    the need for intermediate DataFrames (and thus executes much more quickly):
#        fish_df.groupby('Species')['Weight'].agg(['count', 'std', 'mean', 'min', 'max'])
#
# 4. For extra credit, try the following:
#   * Move around and/or remove functions used for aggregation, and see how the output changes.
#   * Change the variable whose values are summarized to 'Width'.


# Example 9. [Python w/ pandas & saspy] Load a DataFrame into a SAS dataset; execute SAS code
#
# Uncomment the lines of code immediately below, and then execute:

# sas.dataframe2sasdata(fish_df_gsa, table="fish_sds_gsa", libref="Work")
# sas_submit_return_value = sas.submit(
#     '''
#         PROC PRINT DATA=fish_sds_gsa;
#         RUN;
#     ''',
#     results='TEXT'
# )
# sas_submit_results = sas_submit_return_value['LST']
# print_with_title(sas_submit_results, 'SAS results from PROC PRINT applies to new SAS dataset Work.fish_sds_gsa:')

# Notes:
#
# 1. The DataFrame fish_df_gsa, which was created in a cell above from the SAS dataset sashelp.fish, is used to create
#    the new SAS dataset Work.fish_sds_gsa. The SAS PRINT procedure is then called, and the following is printed:
#   * the output returned by PROC PRINT
#
# 2. The sas object, which was created in a cell above, is a persistent connection to a SAS session, and two of its
#    methods are used as follows:
#   * The dataframe2sasdata method writes the contents of the DataFrame fish_df_gsa to the SAS dataset fish_sds_gsa
#     stored in the Work library. (Note: The row indexes of the DataFrame fish_df_gsa are lost when the SAS dataset
#     fish_sds_gsa is created.)
#   * The submit method is used to submit the PROC PRINT step to the SAS kernel, and a dictionary is returned with the
#     following two key-value pairs:
#     - sas_submit_return_value['LST'] is a string comprising the results from executing PROC PRINT, which will be in
#       plain text because the results='TEXT' was used
#     - sas_submit_return_value['LOG'] is a string comprising the plain-text log resulting from executing PROC PRINT
#
# 3. Python strings surrounded by single quotes (e.g., 'Hello, World!') cannot be written across multiple lines of code,
#    whereas strings surrounded by triple quotes (e.g., the argument to the submit method) can.
#
# 4. For extra credit, try the following:
#   * Print the SAS log instead.
#   * Change the SAS procedure used to interact with SAS dataset Work.fish_sds_gsa (e.g., try PROC CONTENTS).

