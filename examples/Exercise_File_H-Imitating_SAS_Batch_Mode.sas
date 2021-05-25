%put Hello, SAS Log!;

data hello;
    greeting = 'Hello, SAS Results!';
run;

proc print data=hello;
run;