# In the name of Allah

from enum import Enum

number = 2 + 3j
number = complex(2, 3)
print(number)

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.INACTIVE.value)

""" 
type()
any()
all()

Complex Data Type:  complex()

abs()
round( , decimal number to round to)

Constants: Enums
list()
"""