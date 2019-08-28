# Everything is better with friends: Executing SAS® code in Python scripts with
# SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019

###############################################################################
# Extra Credit Exercise 3: Imitating the SAS macro processor                  #
###############################################################################

# Lines 11-13 load modules needed for exercises and should be left as-is
from class_setup import print_with_title
from pandas import DataFrame
from saspy import SASsession




###############################################################################
#                                                                             #
# Extra Credit Example 3.                                                     #
# [Python w/ saspy] [Python w/ saspy] Imitate the SAS Macro Processor         #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# sas = SASsession()
# sas_code_fragment = 'PROC MEANS DATA=sashelp.%s; RUN;'
# for dsn in ['fish', 'iris']:
#     sas_submit_return_value = sas.submit(sas_code_fragment % dsn, results='TEXT')
#     print_with_title(sas_submit_return_value['LST'], 'SAS results from PROC MEANS applies to sashelp.%s:' % dsn)


# Notes:
#
# 1. A string object named sas_code_fragment is created with templating
#    placeholder %s, which will be filled using other strings in subsequent
#    uses of sas_code_fragment.
#
# 2. The output of PROC MEANS applied to SAS datasets sashelp.fish and
#    sashelp.iris is then displayed.
#
# 3. The sas object represents a connection to a SAS session and was created
#    when a previous cell was run. Here, sas calls its submit method for each
#    value of the for-loop indexing variable dsn, and the %s portion of
#    sas_code_fragment is replaced by the value of dsn. In other words, the
#    following SAS code is submitted to the SAS kernel:
#        proc means data=sashelp.fish; run;
#        proc means data=sashelp.iris; run;
#
# 4. The same outcome could also be achieved with the following SAS macro code:
#        %macro loop();
#             %let dsn_list = fish iris;
#             %do i = 1 %to 2;
#                 %let dsn = %scan(&dsn_list.,&i.);
#                 proc means data=sashelp.&dsn.;
#                 run;
#             %end;
#        %mend;
#        %loop()
#
#   However, note the following differences:
#    * Python allows us to concisely repeat an arbitrary block of code by
#      iterating over a list using a for-loop. In other words, the body of the
#      for-loop (meaning everything indented underneath it, since Python uses
#      indentation to determine scope) is repeated for each string in the list
#      ['fish','iris'].
#    * The SAS macro facility only provides do-loops based on numerical index
#      variables (the macro variable i above), so clever tricks like implicitly
#      defined arrays (macro variable dsn_list above) need to be used together
#      with functions like %scan to extract a sequence of values.
