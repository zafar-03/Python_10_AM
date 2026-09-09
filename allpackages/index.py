# print("Main File")
# Module  

# import 
# 1. 
# import calculator

# calculator.addition(1,2)
# calculator.subtraction(1,2)
# calculator.multiplication(3,2)
# calculator.division(1,2)

# 2.
# from calculator import addition,subtraction,division,multiplication

# addition(1,2)
# subtraction(1,2)
# multiplication(3,2)
# division(1,2)


# 3.
# import calculator as calc

# calc.addition(1,2)
# calc.subtraction(1,2)
# calc.multiplication(3,2)
# calc.division(1,2)


# print("Package")

"""
it's can contains __init__.py file.
1. 
from package_name import module_name

or 

2. 
from package_name *       (all module)

or

3. 
import packagename
"""

# # 1. 
# from lib import calculator
# from lib import calc
# from lib import calculator,calc

# calculator.addition(1,2)
# calculator.subtraction(1,2)
# calculator.multiplication(3,2)
# calculator.division(1,2)


# calc.addition(1,2)
# calc.subtraction(1,2)
# calc.multiplication(3,2)
# calc.division(1,2)


# from lib import *

# calculator.addition(1,2)
# calculator.subtraction(1,2)
# calculator.multiplication(3,2)
# calculator.division(1,2)


# calc.addition(1,2)
# calc.subtraction(1,2)
# calc.multiplication(3,2)
# calc.division(1,2)



# dir() : 

# import calculator

from lib import calc

print(dir(calc))


import lib   # package 

print(dir(lib))



# import 

# dattime random uuid os fs math 