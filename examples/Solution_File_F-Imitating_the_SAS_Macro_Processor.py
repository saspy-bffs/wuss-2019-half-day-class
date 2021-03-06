# Everything is better with friends: Executing SAS® code in Python scripts with
# SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019


###############################################################################
# Exercise 13: Imitating the SAS macro processor                              #
###############################################################################

# Lines 12-14 load modules needed for exercises and should be left as-is
from class_setup import print_with_title
from saspy import SASsession
sas = SASsession()




###############################################################################
#                                                                             #
# Exercise 13. [Python w/ saspy] Imitate the SAS Macro Processor              #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# Original Version
sas_code_fragment = 'proc means data=sashelp.%s; run;'
for dsn in ['fish', 'iris']:
    sas_submit_return_value = sas.submit(
        sas_code_fragment % dsn,
        results='TEXT'
    )
    print_with_title(
        sas_submit_return_value['LST'],
        'SAS results from PROC MEANS applies to sashelp.%s:' % dsn
    )

# Change the SAS procedure used
for dsn in ['fish', 'iris']:
    print(f'PROC PRINT applied to sashelp.{dsn}:')
    print(
        sas.submit(
            f'proc print data=sashelp.{dsn}(obs=5); run;',
            results='TEXT'
        )['LST']
    )

# Change the datasets used
for dsn in ['cars', 'class']:
    print(f'PROC MEAN applied to sashelp.{dsn}:')
    print(
        sas.submit(
            f'proc means data=sashelp.{dsn}; run;',
            results='TEXT'
        )['LST']
    )

# Print out the SAS logs
for dsn in ['fish', 'iris']:
    print(f'PROC MEAN applied to sashelp.{dsn} log:')
    print(
        sas.submit(
            f'proc means data=sashelp.{dsn}; run;',
            results='TEXT'
        )['LOG']
    )


# Notes:
#
# 1. A string object named sas_code_fragment is created with templating
#    placeholder %s, which will be filled using other strings in subsequent
#    uses of sas_code_fragment.
#
# 2. The output of PROC MEANS applied to SAS datasets sashelp.fish and
#    sashelp.iris is then displayed.
#
# 3. The sas object, which was created at the beginning of this file, is a
#    persistent connection to a SAS session. Here, its submit method is used
#    for each value of the for-loop indexing variable dsn, and the %s portion
#    of sas_code_fragment is replaced by the value of dsn. In other words, the
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
#
# 5. For additional practice, try any or all of the following:
#    * Change the SAS procedure used.
#    * Change the datasets used (e.g., a list of all SASHELP datasets is
#      available at https://support.sas.com/documentation/tools/sashelpug.pdf).
#    * Print out the SAS logs, rather than procedure output.
