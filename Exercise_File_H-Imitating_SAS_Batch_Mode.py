# Everything is better with friends: Executing SAS® code in Python scripts with
# SASPy, and turbocharging your SAS programming with open-source tooling
#
# Half-day class, Western Users of SAS Software (WUSS) 2019


###############################################################################
# Exercises 18: Imitating SAS Batch Mode                                      #
###############################################################################

# Lines 12-15 load modules needed for exercises and should be left as-is
from datetime import datetime
from pathlib import Path
from saspy import SASsession
sas = SASsession()




###############################################################################
#                                                                             #
# Exercise 18. [Python w/ saspy] Imitate SAS Batch Mode                       #
#                                                                             #
# Instructions: Uncomment the code immediately below, and then execute        #
#                                                                             #
###############################################################################


# sas_job_id = sas.symget("SYSJOBID")
#
# sas_input_filename = 'Exercise_File_H-Imitating_SAS_Batch_Mode.sas'
# sas_input_file = Path('.') / sas_input_filename
#
# sas_output_directory = Path('./sas_output')
# sas_output_directory.mkdir(parents=True, exist_ok=True)
#
# current_timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
# sas_output_filename_stem = f'{current_timestamp}-job_id_{sas_job_id}'
# sas_log_file = sas_output_directory / f'{sas_output_filename_stem}.log'
# sas_results_file = sas_output_directory / f'{sas_output_filename_stem}.txt'
#
# with open(sas_input_file) as fp:
#     sas_submit_return_value = sas.submit(fp.read(), results='TEXT')
#
# with open(sas_log_file, 'w') as fp:
#     fp.write(sas_submit_return_value['LOG'])
#
# with open(sas_results_file, 'w') as fp:
#     fp.write(sas_submit_return_value['LST'])
#
# print(f'SAS file {sas_input_file} executed with job id {sas_job_id}')
# print(f'Log written to file {sas_log_file}')
# print(f'Results written to file {sas_results_file}')


# Notes:
#
# 1. Several variables are created to specify a SAS code file to be input, a
#    directory for output (which is created if it doesn't already exist), and
#    files to write output to. Then, after the files are written, the following
#    are printed:
#    * the name of the input file, as well as the job id for the SAS session it
#      was submitted to
#    * the name of the file the SAS log was written to, which includes a
#      timestamp for when this example file was run
#    * the name of the file SAS results were written to, also timestamped
#
# 2. The sas object, which was created at the beginning of this file, is a
#    persistent connection to a SAS session, and its symget method is used to
#    get the value of the automatic SAS macro variable SYSJOBID, which contains
#    the job id for the SAS session. (The companion method symput could also be
#    used to create a new SAS macro variable.) In addition, the submit method
#    is used to submit the contents of the input file to the SAS kernel, and a
#    dictionary is returned with the following two key-value pairs:
#      - sas_submit_return_value['LOG'] is a string comprising the plain-text
#        log resulting from executing the input file
#      - sas_submit_return_value['LST'] is a string comprising the results from
#        executing the input file, which will be in plain text because the
#        results='TEXT' option was used
#
# 3. File paths are handled using features of the pathlib module, which allow
#    a base file Path object to be created without worrying about the
#    underlying operating system and its conventions for specifying file paths.
#    Then, additional portions of a file path can be added to the Path object
#    using the forward-slash operator (/), which is the typical file-path
#    separator used in the Unix operating system.
#
#    For example, the object Path('.') means the current directory (using the
#    standard Unix convention), and so
#        Path('.') / sas_input_filename
#    means the path './Exercise_File_H-Imitating_SAS_Batch_Mode.sas', i.e., the
#    file named Exercise_File_H-Imitating_SAS_Batch_Mode.sas in the current
#    directory.
#
# 4. All file interactions are handled with "context managers", which use the
#    keyword "with" and indentation to define their scope. (Think for-loop,
#    but with everything indented only executed once.) Context managers are a
#    shortcut in SAS for managing resources, like file access, by automatically
#    handling the opening of a file and then closing the file after the scope
#    is executed.
#
# 5. With a bit more code, this example could be turned into a completely
#    general command-line utility with the name of the SAS file to be executed
#    passed as a command-line argument.
#
# 6. For additional practice, try changing the results type from TEXT output to
#    HTML, changing the results filename extension to .html, and then viewing
#    the resulting .html file in a web browser.
