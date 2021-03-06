# Everything is better with friends: Executing SAS® code in Python scripts with
# SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019


###############################################################################
# Exercises 14-17: Common DataFrame Operations                                #
###############################################################################

# Lines 12-14 load modules needed for exercises and should be left as-is
from class_setup import print_with_title
from saspy import SASsession
sas = SASsession()




###############################################################################
#                                                                             #
# Exercise 14. [Python w/ saspy] Adding and dropping columns                  #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# Original Version
class_df = sas.sasdata2dataframe(table='class', libref='sashelp')
print_with_title(class_df.head(), 'The first 5 rows of class_df:')

class_df['BMI'] = (class_df['Weight'] / class_df['Height'] ** 2) * 703
print_with_title(
    class_df.head(),
    'The first 5 rows of class_df after a new column has been added:'
)

class_df.drop(columns=['Height', 'Weight'], inplace=True)
print_with_title(
    class_df.head(),
    'The first 5 rows of class_df after a two columns have been dropped:'
)

# Execute the SAS code equivalent
print('The results of the SAS code equivalent:')
print(
    sas.submit(
        '''
            data class(drop = Height Weight);
                set sashelp.class;
                BMI = (Weight/Height**2)*703;
            run;
            proc print data=class(obs=5);
            run;
        ''',
        results='TEXT'
    )['LST']
)


# Notes:
#
# 1. A DataFrame object named class_df with dimensions 19x5 (19 rows and 5
#    columns) is created from the SAS dataset class in the sashelp library,
#    and the following are printed:
#    * the names of the columns in class_df
#    * the first five rows of class_df after a new column named BMI has been
#      added, using the formula provided by the CDC at https://www.cdc.gov/
#      nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html
#    * the first five rows of class_df after the columns Height and Weight have
#      been dropped, with the inplace=True option used to change
#      class_df itself rather than create a copy with the columns removed
#
# 2. The sas object, which was created at the beginning of this file, is a
#    persistent connection to a SAS session, and its sasdata2dataframe method
#    is used to create class_df.
#
# 3. All subsequent exercises in this file will assume the object class_df
#    exists, so please don't comment out the line creating it.
#
# 4. The same outcome could also be achieved with the following SAS code:
#        data class(drop = Height Weight);
#            set sashelp.class;
#            BMI = (Weight/Height**2)*703;
#        run;
#    However, note the following differences: Python allows us to concisely
#    create a new column by manipulating the entire DataFrame class_df in
#    memory, whereas the SAS DATA step requires rows to be loaded from disk and
#    manipulated individually.
#
# 5. For additional practice, use the sas.submit method to execute the SAS
#    code above, and compare the results.




###############################################################################
#                                                                             #
# Exercise 15. [Python w/ saspy] Merging DataFrame objects                    #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# Original Version
steel_df = sas.sasdata2dataframe(table='steel', libref='sashelp')
print_with_title(steel_df, 'The contents of steel_df')

tourism_df = sas.sasdata2dataframe(table='tourism', libref='sashelp')
print_with_title(tourism_df, 'The contents of tourism_df')

merged_df = steel_df.merge(
    tourism_df,
    left_on='DATE',
    right_on='year',
    how='inner'
)
print_with_title(merged_df, 'The contents of the merged DataFrame')

# Execute the SAS code equivalent
print('The results of the SAS code equivalent:')
print(
    sas.submit(
        '''
            proc sql;
                create table merged as
                    select
                         A.*
                        ,B.*
                    from
                        sashelp.steel as A
                        inner join
                        sashelp.tourism as B
                        on A.DATE = B.year
                ;
            quit;
            proc print data=merged;
            run;
        ''',
        results='TEXT'
    )['LST']
)


# Notes:
#
# 1. Two DataFrame objects named steel_df (44 rows by 2 columns) and tourism_df
#    (29 rows by 8 columns) are created from the SAS datasets steel and tourism
#    in the sashelp library, respectively, and the following are printed:
#    * all rows of steel_df
#    * all rows of tourism_df
#    * all rows of merged_df (15 rows by 10 columns), which was created by
#      merging steel_df with tourism_df based on matching values in the columns
#      DATE and year, respectively
#
# 2. The sas object, which was created at the beginning of this file, is a
#    persistent connection to a SAS session, and its sasdata2dataframe method
#    is used to create steel_df and tourism_df.
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
#    However, note the following differences:
#    * The PROC SQL version is more flexible since the join condition
#      A.DATE = B.year can be changed arbitrarily (not necessarily involving
#      equality), whereas the Python can only merge based on the equality of
#      values in one or more columns.
#    * PROC SQL version can be extended to arbitrarily many tables, whereas the
#      Python version can only operate on two DataFrame objects at a time.
#
# 4. If you see a message about datasets not existing, a SAS installation
#    without the product SAS/ETS has been chosen. Should this happen, please
#    comment out all code for this exercise.
#
# 5. For additional practice, use the sas.submit method to execute the SAS
#    code above, and compare the results.




###############################################################################
#                                                                             #
# Exercise 16. [Python w/ saspy] Appending DataFrame objects                  #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# Original Version
countseries_df = sas.sasdata2dataframe(table='countseries', libref='sashelp')
print_with_title(countseries_df, 'The contents of countseries_df')

countseries_df.columns = ['Date', 'Amount']
print_with_title(countseries_df, 'countseries_df with renamed columns')

rockpit_df = sas.sasdata2dataframe(table='rockpit', libref='sashelp')
print_with_title(rockpit_df, 'The contents of rockpit_df')

rockpit_df.columns = [column.title() for column in rockpit_df.columns]
print_with_title(rockpit_df, 'rockpit_df with renamed columns')

appended_df = countseries_df.append(rockpit_df)
print_with_title(appended_df, 'The results of appending the DataFrames')

# Execute the SAS code equivalent
print('The results of the SAS code equivalent:')
print(
    sas.submit(
        '''
            proc sql;
                create table appended as
                    select Date as Date, Units as Amount from sashelp.countseries
                    union all corr
                    select DATE as Date, AMOUNT as Amount from sashelp.rockpit
                ;
            quit;
            proc print data=appended(obs=5);
            run;
        ''',
        results='TEXT'
    )['LST']
)


# Notes:
#
# 1. Two DataFrame objects named countseries_df (108 rows by 2 columns) and
#    rockpit_df (6 rows by 8 columns) are created from the SAS datasets
#    countseries and rockpit in the sashelp library, respectively, and the
#    following are printed:
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
# 2. The sas object, which was created at the beginning of this file, is a
#    persistent connection to a SAS session, and its sasdata2dataframe method
#    is used to create countseries_df and rockpit_df.
#
# 3. The same outcome could also be achieved with the following SAS code:
#         proc sql;
#             create table appended as
#                 select Date as Date, Units as Amount from sashelp.countseries
#                 union all corr
#                 select DATE as Date, AMOUNT as Amount from sashelp.rockpit
#             ;
#         quit;
#   However, note the following differences:
#    * The PROC SQL version is more flexible since the set operation union
#      could be replaced by other operations (e.g., intersect to get just rows
#      in common), whereas more work would be needed to achieve the same result
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
#    without the product SAS/ETS has been chosen. Should this happen, please
#    comment out all code for this exercise.
#
# 6. For additional practice, use the sas.submit method to execute the SAS
#    code above, and compare the results.




###############################################################################
#                                                                             #
# Exercise 17. [Python w/ saspy] Indexing a column in a DataFrame             #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# Original Version
class_df.set_index('Name', inplace=True)
print_with_title(
    class_df.head(),
    'The first 5 rows of class_df after a column has been set as an index:'
)
print_with_title(
    class_df.loc['Alfred'],
    'The row corresponding to "Name"="Alfred":'
)

# Execute the SAS code equivalent
print('The results of the SAS code equivalent:')
print(
    sas.submit(
        '''
        proc sql;
            create table class(index=(name)) as
                select * from sashelp.class
            ;
        quit;
        data alfreds_row;
            set class(idxwhere=yes);
            where name='Alfred';
        run;
        proc print data=alfreds_row;
        run;
        ''',
        results='TEXT'
    )['LST']
)


# Notes:
#
# 1. The DataFrame fish_df_gsa, which was created in an exercise above from the
#    SAS dataset sashelp.class, is used to print the following:
#    * the first five rows of class_df
#    * the first five rows of class_df after the column 'Name' has been set as
#      a row index, eliminating the previously used default numerical row index
#    * the row in class_df corresponding to 'Name'='Alfred'
#
# 2. The sas object represents a connection to a SAS session and was created
#    when a previous cell was run. Here, sas calls its sasdata2dataframe method
#    to create class_df.
#
# 3. Because an index column was set, the row corresponding to Alfred can be
#    retrieved directly using an extremely efficient lookup, which is
#    essentially how Python looks up values in a dictionary by key. (Think
#    logarithmic time, rather than linear.) Without an index, all rows would
#    need to be examined individually. A common way to do this is as follows:
#        class_df[class_df.Name == 'Alfred']
#    In other words, we'd need to create a "row mask" based on the condition
#    class_df.Name == 'Alfred', meaning a series of the values True and False,
#    and then ask for the rows corresponding to the values of True.
#
# 4. While index columns make querying a DataFrame faster, there's also a
#    trade-off. More memory will be needed to maintain the index, and some
#    operations (e.g., inserting new rows or modifying existing ones) can
#    become slower. For small DataFrames, there's no reason not to use indexes.
#    However, for large DataFrames, indexes are best used when we want to query
#    much more often than we want to change values.
#
# 5. The same outcome could also be achieved with the following SAS code:
#         proc sql;
#             create table class(index=(name)) as
#                 select * from sashelp.class
#             ;
#         quit;
#         data alfreds_row;
#             set class(idxwhere=yes);
#             where name='Alfred';
#         run;
#    However, note the following differences: Python allows us to set one (or
#    more) columns as indexes for a DataFrame, allowing rows to be selected by
#    implicitly querying the values in the index column(s). Since a DataFrame
#    is stored entirely in memory, this allows specific rows to be retrieved
#    much more efficiently than the SAS DATA step, which requires rows to be
#    loaded from disk.
#
# 6. For additional practice, use the sas.submit method to execute the SAS
#    code above, and compare the results.
#
# 7. If you're interested in learning more about DataFrames, we recommend
#    https://nbviewer.jupyter.org/github/justmarkham/pandas-videos/tree/master/
