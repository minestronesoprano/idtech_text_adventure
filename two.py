import random

lower_bound = 0
upper_bound = 12
print(random.randint(lower_bound, upper_bound))  # inclusive of bounds, goes 1 to 12


def function_name(max_int):        # need two blank lines before and after method/class definition
    hi = random.randrange(lower_bound, max_int)      # non-inclusive bounds, goes 2 to 11
    return hi               # no preassigned return type, an return whatever or be void if no return


number = function_name(upper_bound)    # call a method, if assigning to a var, var must be consistent with return.
print(number)   # can have parameters too

""" arrays are called lists. initialize with just values like so
[1, 2, 3, 4} or ["a", "b", "c", "d"]

use the sort() method, syntax is list_name.sort(), to sort in alphabetic or numerical order

use append(item_to_append)
or insert(position, list_to_insert) to move later numbers backward, not replace anything.

pop() removes the last value
pop(position) removes that position
remove(value) takes out a specific value"""

