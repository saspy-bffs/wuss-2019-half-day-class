# Everything is better with friends: Executing SAS® code in Python scripts with
# SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019


###############################################################################
# Extra Credit Exercise 0: Getting SAS session information                    #
###############################################################################

# Lines 12-14 load modules needed for exercises and should be left as-is
from class_setup import print_with_title
from pandas import DataFrame
from saspy import SASsession




###############################################################################
#                                                                             #
# Extra Credit Example 1. [Python w/ saspy] Get information about a SAS       #
# session                                                                     #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# sas = SASsession()
# sas_submit_return_value = sas.submit('PROC PRODUCT_STATUS; RUN;')
# sas_submit_log = sas_submit_return_value['LOG']
# print_with_title(sas_submit_log, 'SAS log from PROC PRODUCT_STATUS:')


# Notes:
#
# 1. The SAS PRODUCT_STATUS procedure is called, and the following is printed:
#    * the log returned by PROC PRODUCT_STATUS
#
# 2. The sas object, which was created in a cell above, is a persistent
#    connection to a SAS session, and its submit method is used to submit the
#    PROC PRODUCT_STATUS step to the SAS kernel. A dictionary is returned with
#    the following two key-value pairs:
#    * sas_submit_return_value['LST'] is a string comprising the results from
#      executing PROC PRODUCT_STATUS, which is empty because no output is
#      produced by this procedure
#    * sas_submit_return_value['LOG'] is a string comprising the plain-text log
#      resulting from executing PROC PRODUCT_STATUS
#
# 3. Since a plain-text value is being printed, Python's print function is used
#    to render the result.
#
# 4. Like the Python command help('modules') gives us information about the
#    Python modules available to our Python session, the PRODUCT_STATUS
#    procedure gives us information about the products available in the SAS
#    environment we're connected to.
