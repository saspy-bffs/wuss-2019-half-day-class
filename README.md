[![Python 3.7](https://img.shields.io/badge/python-3.7-brightgreen.svg)](#prerequisites)  [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  [![Gitter](https://img.shields.io/gitter/room/saspy-bffs/community.svg?color=777777)](https://gitter.im/saspy-bffs/community)

# Everything is better with friends: Executing SAS code in Python scripts with SASPy, and turbocharging your SAS programming with open-source tooling

### Materials from a Half-Day Class at [Western Users of SAS Software](https://www.wuss.org/) in Seattle, Washington, on September 4, 2019.

Materials provided:

- Software [setup instructions](WUSS2019-Class-Everything_Is_Better_With_Friends-setup_instructions.pdf)

- Seven Exercise files:
  * [Exercise_File_A-Getting_Started_with_Python.py](Exercise_File_A-Getting_Started_with_Python.py)
  * [Exercise_File_B-Common_Python_Data_Structures.py](Exercise_File_B-Common_Python_Data_Structures.py)
  * [Exercise_File_C-SASPy_Data_Round_Trip.py](Exercise_File_C-SASPy_Data_Round_Trip.py)
  * [Exercise_File_D-Getting_SASPy_Environment_Info.py](Exercise_File_D-Getting_SASPy_Environment_Info.py)
  * [Exercise_File_E-SASPy_Convenience_Methods.py](Exercise_File_E-SASPy_Convenience_Methods.py)
  * [Exercise_File_F-Imitating_the_SAS_Macro_Processor.py](Exercise_File_F-Imitating_the_SAS_Macro_Processor.py)
  * [Exercise_File_G-Common_DataFrame_Operations.py](Exercise_File_G-Common_DataFrame_Operations.py)

- Seven (Possible) Solutions files
  * [Solution_File_A-Getting_Started_with_Python.py](Solution_File_A-Getting_Started_with_Python.py)
  * [Solution_File_B-Common_Python_Data_Structures.py](Solution_File_B-Common_Python_Data_Structures.py)
  * [Solution_File_C-SASPy_Data_Round_Trip.py](Solution_File_C-SASPy_Data_Round_Trip.py)
  * [Solution_File_D-Getting_SASPy_Environment_Info.py](Solution_File_D-Getting_SASPy_Environment_Info.py)
  * [Solution_File_E-SASPy_Convenience_Methods.py](Solution_File_E-SASPy_Convenience_Methods.py)
  * [Solution_File_F-Imitating_the_SAS_Macro_Processor.py](Solution_File_F-Imitating_the_SAS_Macro_Processor.py)
  * [Solution_File_G-Common_DataFrame_Operations.py](Solution_File_G-Common_DataFrame_Operations.py)

All development was done under Windows 10 with Python 3.7 and SAS 9.4 locally installed. Any deviation from this setup might require modifications to example code.

## Prerequisites

All examples assume a reasonably current version of Python 3.7 (or later) is installed, along with the modules specified in [requirements.txt](requirements.txt).

In addition, Exercise Files C-G require access to installations of Java SE ([https://www.oracle.com/technetwork/java/javase/](https://www.oracle.com/technetwork/java/javase/)) and SAS 9.4 ([https://www.sas.com/en_us/software/sas9.html](https://www.sas.com/en_us/software/sas9.html)), and the instructions in [sascfg_personal-example.py](sascfg_personal-example.py) should be used to create a file called `sascfg_personal.py` in the project directory. Exercise File G also requires access to SAS/ETS ([https://www.sas.com/en_us/software/ets.html](https://www.sas.com/en_us/software/ets.html)).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors
* [ilankham](https://github.com/ilankham)
* [mtslaugh](https://github.com/mtslaugh)

## Disclaimer

This project is in no way affiliated with SAS Institute Inc.
