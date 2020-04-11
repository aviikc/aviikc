'''
functions are typically declared as:

def function_name(comma_separated_list_of_parameters):
    statement

'''

'''
    A PYTHON FILE (*.py file) IS GENERALLY CALLED A MODULE 
    https://docs.python.org/3/tutorial/modules.html 

A python module may contain various definations of variables, functions or classes

 If you run the program automatically or typically in terminal or command prompt if 
 we change directory to the one containing this 02_declaring_functions.py  
 and run the python file using 


    python 02_declaring_functions.py

            or

    python3 02_declaring_functions.py

  The function will not be executed.
 '''



'''
    To execute functions we shall use the statement below.

    if __name__== "__main__":
        function_name()

Every python module has a built in variable called __name__ containing the name of the 
module(in this case "02_declaring_functions.py"). When the module itself is being run as 
the script, this variable __name__ is assigned the string "__main__" designating it to be
a __main__ module.
https://docs.python.org/3/library/__main__.html

 '''