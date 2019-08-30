# Everything is better with friends: Executing SAS® code in Python scripts with
# SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019


###############################################################################
# Exercise 10: Getting SASPy Environment Info                                 #
###############################################################################

# Lines 12-14 load modules needed for exercises and should be left as-is
from class_setup import print_with_title
from saspy import SASsession
sas = SASsession()




###############################################################################
#                                                                             #
# Exercise 10. [Python w/ saspy] Get info about a SAS session                 #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# sas_submit_return_value = sas.submit('PROC PRODUCT_STATUS; RUN;')
# sas_submit_log = sas_submit_return_value['LOG']
# print_with_title(sas_submit_log, 'SAS log from PROC PRODUCT_STATUS:')


# Notes:
#
# 1. The SAS PRODUCT_STATUS procedure is called, and the following is printed:
#    * the log returned by PROC PRODUCT_STATUS
#
# 2. As before, the sas object represents a connection to a SAS session, and
#    its submit method is used to submit the PROC PRODUCT_STATUS step to the
#    SAS kernel. A dictionary is returned with the following key-value pairs:
#    * sas_submit_return_value['LST'] is a string comprising the results from
#      executing PROC PRODUCT_STATUS, which is empty because no output is
#      produced by this procedure
#    * sas_submit_return_value['LOG'] is a string comprising the plain-text log
#      resulting from executing PROC PRODUCT_STATUS
#
# 3. Like the Python command help('modules') gives us information about the
#    Python modules available to our Python session, the PRODUCT_STATUS
#    procedure gives us information about the products available in the SAS
#    environment we're connected to.
#
# 4. For additional practice, try any or all of the following:
#    * Verify the output from PROC PRODUCT_STATUS is empty.
#    * Compare the output of PROC PRODUCT_STATUS to PROC SETINIT.
#    * Refactor the sas.submit call to match Exercise 9, including
#      triple-quotes (''') around the argument and embedded line breaks.
