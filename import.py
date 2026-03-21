import pandas as pd
import math
from math import sqrt, floor

from dummy import greet, bye

# pd.read_csv("data.csv")

a = sqrt(16)
print(floor(a))

# dir() function returns a list of the attributes and methods of any object
# (functions, modules, strings, lists, dictionaries etc.)
b = dir(math)
print(b)

greet()
print(bye)
