'''
When a program fails to yeild the desirable result we say it contains a bug.
A bug could be because of different zero division, or non matching data type,
uninitialized variable,etc.

The process of discovering the bugs and making them bug free is called debugging.

'''

# List of error types are attached as python_errors.py

# One of the ways of catching error in python is using a module called pdb
# Its not one of the best debuggers in python, but its cross platform and is included in the standard library.
# once in the command prompt or terminal and in the same directory as the module to be debugged type

# python -m pdb my_program.py


# or we can include inside the module
'''
import pdb
pdb.set_trace()
'''

# This is preferably not included at the beginning or end of the module but generally before the last command.