# Everything is better with friends:
# Executing SAS® code in Python scripts with SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019
#
# Extra Credit:  5-6 Additional pandas operations

# Lines 8 through 22 load necessary modules and define a function to format output.
# Execute without editing

# load all third-party modules needed for examples
from pandas import DataFrame
from saspy import SASsession

sas = SASsession()


# define utility function to print linebreak-padded output with a title and optional line of 80 stars afterward
def print_with_title(output, title='', linebreaks_before=2, linebreaks_after=2, put_stars_after=True):
    print('\n' * linebreaks_before + title + '\n' * 2, output, '\n' * linebreaks_after, sep='')
    if put_stars_after:
        print('*' * 80)


# Extra Credit Example 5. [Python w/ saspy] Adding and dropping columns from a DataFrame
#
# Type the following code into the cell labelled [ ]: immediately below, and then run that cell using Shift-Enter:

# class_df = sas.sasdata2dataframe(table='class', libref='sashelp')
# print_with_title(class_df.head(), 'The first 5 rows of class_df:')
# class_df['BMI'] = (class_df['Weight'] / class_df['Height'] ** 2) * 703
# print_with_title(class_df.head(), 'The first 5 rows of class_df after a new column has been added:')
# class_df.drop(columns=['Height', 'Weight'], inplace=True)
# print_with_title(class_df.head(), 'The first 5 rows of class_df after a two columns have been dropped:')

# Notes:
# 1. A DataFrame object named class_df with dimensions 19x5 (19 rows and 5 columns) is created from the SAS dataset
#    class in the sashelp library, and the following are printed with blank lines between them:
#   * the names of the columns in class_df
#   * the first five rows of class_df after a new column named BMI has been added, using the formula
#     (https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html) provided by the CDC
#   * the first five rows of class_df after the columns Height and Weight have been dropped, with the inplace=True
#     option used to change class_df itself rather than create a copy with the columns removed
#
# 2. The sas object represents a connection to a SAS session and was created when a previous cell was run. Here, sas
#    calls its sasdata2dataframe method to create class_df.
#
# 3. The same outcome could also be achieved with the following SAS code:
#        data class(drop = Height Weight);
#            set sashelp.class;
#            BMI = (Weight/Height**2)*703;
#        run;
#    However, note the following differences: Python allows us to concisely create a new column by manipulating the
#    entire DataFrame class_df in memory, whereas the SAS DATA step requires rows to be loaded from disk and manipulated
#    individually.


# Extra Credit Example 8. [Python w/ saspy] Indexing a column in a DataFrame
#
# Type the following code into the cell labelled [ ]: immediately below, and then run that cell using Shift-Enter:

# class_df.set_index('Name', inplace=True)
# print_with_title(class_df.head(), 'The first 5 rows of class_df after a column has been set as an index:')
# print_with_title(class_df.loc['Alfred', :], 'The row corresponding to "Name"="Alfred":')

# Notes:
#
# 1. A DataFrame object named class_df with dimensions 19x5 (19 rows and 5 columns) is created from the SAS dataset
#    class in the sashelp library, and the following are printed with blank lines between them:
#   * the first five rows of class_df
#   * the first five rows of class_df after the column 'Name' has been set as its index, which eliminates the previously
#     used default numerical index column and makes querying by student more streamlined
#   * the row in class_df corresponding to 'Name'='Alfred', which would have required a more complex operation to first
#     look up the row corresponding to Alfred if an index hadn't been created
#
# 2. The sas object represents a connection to a SAS session and was created when a previous cell was run. Here, sas
#     calls its sasdata2dataframe method to create class_df.
#
# 3. The same outcome could also be achieved with the following SAS code:
#        proc sql;
#            create table class(index=(names)) as
#                select * from sashelp.class
#           ;
#       quit;
#
#        data alfreds_row;
#            set class(idxwhere=yes);
#            where name='Alfred';
#        run;
#    However, note the following differences: Python allows us to set one (or more) columns as indexes for a DataFrame,
#    allowing rows to be selected by implicitly querying the values in the index column(s). Since a DataFrame is stored
#    entirely in memory, this allows specific rows to be retrieved much more efficiently than the SAS DATA step, which
#    requires rows to be loaded from disk and inspected individually.
