# Everything is better with friends: Executing SAS® code in Python scripts with
# SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019


###############################################################################
# Extra Credit Exercises:  4-7 Additional pandas operations                   #
###############################################################################

# Lines 12-14 load modules needed for exercises and should be left as-is
from class_setup import print_with_title
from pandas import DataFrame
from saspy import SASsession




###############################################################################
#                                                                             #
# Extra Credit Example 4.                                                     #
# [Python w/ saspy] Adding and dropping columns from a DataFrame              #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# sas = SASsession()
# class_df = sas.sasdata2dataframe(table='class', libref='sashelp')
#
# print_with_title(class_df.head(), 'The first 5 rows of class_df:')
# class_df['BMI'] = (class_df['Weight'] / class_df['Height'] ** 2) * 703
# print_with_title(
#   class_df.head(),
#   'The first 5 rows of class_df after a new column has been added:'
# )
# class_df.drop(columns=['Height', 'Weight'], inplace=True)
# print_with_title(
#     class_df.head(),
#     'The first 5 rows of class_df after a two columns have been dropped:'
# )


# Notes:
# 1. A DataFrame object named class_df with dimensions 19x5 (19 rows and 5
#    columns) is created from the SAS dataset class in the sashelp library,
#    and the following are printed with blank lines between them:
#    * the names of the columns in class_df
#    * the first five rows of class_df after a new column named BMI has been
#      added, using the formula
#      (https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html)
#      provided by the CDC
#    * the first five rows of class_df after the columns Height and Weight have
#      been dropped, with the inplace=True option used to change
#      class_df itself rather than create a copy with the columns removed
#
# 2. The sas object represents a connection to a SAS session and was created
#    when a previous cell was run. Here, sas calls its sasdata2dataframe method
#    to create class_df.
#
# 3. The same outcome could also be achieved with the following SAS code:
#        data class(drop = Height Weight);
#            set sashelp.class;
#            BMI = (Weight/Height**2)*703;
#        run;
#    However, note the following differences: Python allows us to concisely
#    create a new column by manipulating the
#    entire DataFrame class_df in memory, whereas the SAS DATA step requires
#    rows to be loaded from disk and manipulated
#    individually.




###############################################################################
#                                                                             #
# Extra Credit Example 5. [Python w/ saspy] Merging DataFrame objects         #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################

#
# steel_df = sas.sasdata2dataframe(table='steel', libref='sashelp')
# tourism_df = sas.sasdata2dataframe(table='tourism', libref='sashelp')
# merged_df = steel_df.merge(tourism_df,left_on='DATE', right_on='year')
# print_with_title(steel_df, 'The contents of steel_df')
# print_with_title(tourism_df, 'The contents of tourism_df')
# print_with_title(merged_df, 'The contents of the merged DataFrame')


# Notes:
#
# 1. Two DataFrame objects named steel_df (44 rows by 2 columns) and tourism_df
#    (29 rows by 8 columns) are created from the SAS datasets steel and tourism
#    in the sashelp library, respectively, and the following are printed with
#    blank lines between them:
#    * all rows of steel_df
#    * all rows of tourism_df
#    * all rows of merged_df (15 rows by 10 columns), which was created by
#      merging steel_df with tourism_df based on matching values in the columns
#      DATE and year, respectively
#
# 2. The sas object represents a connection to a SAS session and was created
#    when a previous cell was run. Here, sas calls its sasdata2dataframe method
#    to create steel_df and tourism_df.
#
# 3. The same outcome could also be achieved with the following SAS code:
#         proc sql;
#             create table merged as
#                 select
#                      A.*
#                     ,B.*
#                 from
#                     sashelp.steel as A
#                     inner join
#                     sashelp.tourism as B
#                     on A.DATE = B.year
#             ;
#         quit;
#
#    However, note the following differences:
#    * The PROC SQL version is more flexible since the join condition
#      A.DATE = B.year can be changed arbitrarily
#      (not necessarily involving equality), whereas the Python can only merge
#      based on the equality of values in one or more columns.
#    * PROC SQL version can be extended to arbitrarily many tables, whereas the
#      Python version can only operate on two DataFrame objects at a time.
# 4. If you see a message about datasets not existing, a SAS installation
#    without the product SAS/ETS has been chosen.




###############################################################################
#                                                                             #
# Extra Credit Example 6. [Python w/ saspy] Appending DataFrame objects       #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# countseries_df = sas.sasdata2dataframe(table='countseries', libref='sashelp')
# print_with_title(countseries_df, 'The contents of countseries_df')
# countseries_df.columns = ['Date', 'Amount']
# print_with_title(countseries_df, 'countseries_df with renamed columns')
#
# rockpit_df = sas.sasdata2dataframe(table='rockpit', libref='sashelp')
# print_with_title(rockpit_df, 'The contents of rockpit_df')
# rockpit_df.columns = [column.title() for column in rockpit_df.columns]
# print_with_title(rockpit_df, 'rockpit_df with renamed columns')
#
# appended_df = countseries_df.append(rockpit_df)
# print_with_title(appended_df, 'The results of appending the DataFrames')


# Notes:
#
# 1. Two DataFrame objects named countseries_df (108 rows by 2 columns) and
#    rockpit_df (6 rows by 8 columns) are created from the SAS datasets
#    countseries and rockpit in the sashelp library, respectively, and the
#    following are printed with blank lines between them:
#    * the first five rows of countseries_df before its columns are renamed
#    * all rows of countseries_df after its columns are renamed by providing a
#      new list of column names
#    * all rows of rockpit_df before its columns are renamed
#    * all rows of rockpit_df after its columns are renamed using a list
#      comprehension in order to have the column 'DATE' match 'Date' in
#      countseries_df (where, e.g., 'DATE'.title() results in 'Date' since
#      title is the Python equivalent of the SAS DATA step function propcase)
#    * all rows of appended_df (114 rows by 3 columns), which was created by
#      appending countseries_df and rockpit_df
#
# 2. The sas object represents a connection to a SAS session and was created
#    when a previous cell was run. Here, sas calls its sasdata2dataframe method
#    to create countseries_df and rockpit_df.
#
# 3. The same outcome could also be achieved with the following SAS code:
#         proc sql;
#             create table appended as
#                 select Date as Date, Units as Amount from sashelp.countseries
#                 union all corr
#                 select DATE as Date, AMOUNT as Amount from sashelp.rockpit
#             ;
#         quit;
#
#   However, note the following differences:
#    * The PROC SQL version is more flexible since the set operation union
#      could be replaced by other operations (e.g., intersect to get just rows
#      in column), whereas more work would be needed to achieve the same result
#      in Python.
#    * The PROC SQL version can be extended to arbitrarily many tables, whereas
#      the Python version can only operate on two DataFrame objects at a time.
#    * The PROC SQL version doesn't require the use of column aliases to change
#      case (e.g., DATE as Date) since the SAS implementation of SQL is not
#      case sensitive. However, it's been included above to exactly mirror the
#      Python version.
#
# 4. As an alternative to carefully renaming columns, we could have also begun
#    this example with sas.submit('OPTIONS VALIDVARNAME=UPCASE;'), which would
#    have converted all SAS dataset column names to uppercase before import.
#
# 5. If you see a message about datasets not existing, a SAS installation
#    without the product SAS/ETS has been chosen.




###############################################################################
#                                                                             #
# Extra Credit Example 7. [Python w/ saspy] Indexing a column in a DataFrame  #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# class_df.set_index('Name', inplace=True)
# print_with_title(
#   class_df.head(),
#   'The first 5 rows of class_df after a column has been set as an index:'
# )
# print_with_title(
#   class_df.loc['Alfred', :],
#   'The row corresponding to "Name"="Alfred":'
# )


# Notes:
#
# 1. A DataFrame object named class_df with dimensions 19x5 (19 rows and 5
#    columns) is created from the SAS dataset class in the sashelp library, and
#    the following are printed with blank lines between them:
#    * the first five rows of class_df
#    * the first five rows of class_df after the column 'Name' has been set as
#      its index, which eliminates the previously used default numerical index
#      column and makes querying by student more streamlined
#    * the row in class_df corresponding to 'Name'='Alfred', which would have
#      required a more complex operation to first look up the row corresponding
#      to Alfred if an index hadn't been created
#
# 2. The sas object represents a connection to a SAS session and was created
#    when a previous cell was run. Here, sas calls its sasdata2dataframe method
#    to create class_df.
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
#    However, note the following differences: Python allows us to set one (or
#    more) columns as indexes for a DataFrame, allowing rows to be selected by
#    implicitly querying the values in the index column(s). Since a DataFrame
#    is stored entirely in memory, this allows specific rows to be retrieved
#    much more efficiently than the SAS DATA step, which requires rows to be
#    loaded from disk and inspected individually.
