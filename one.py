# import this # this adds a nice poems into the console

print("Hello World")
number_of_donuts = 3  # no variable type for int, String, boolean, etc.
# floats exist, and take precedence like floats and doubles in Java
# hashtag space is a single comment
print(number_of_donuts)

donut_name = "Kepler"  # Strings still in quotations
# can use " or ' then use the other inside
print("hello 'me' hi")
print(donut_name)

donut_exists = False  # booleans capitalized

"""name = input("What's your character's name?")  # no scanners or objects
print(name + " hello")  # same + between vars, spaces around + necessary

number_string = input("enter a number")
print(number_string)
print(int(number_string) + 5)"""   # casting to int is int("String") but cannot be nested. one function at a time.

# \n goes to a new line, and \t goes to a new tab, when inside a string
# the two characters \" will put in quotation marks in a string, will work with single and double quotes
print('\ngoogle\'goo\tgle\'hi')

hi = """line 1
line 2
line 3"""
print(hi)   # triple quotes are a multiline string, as space matters

maybe = isinstance(donut_exists, int)   # crazy program thinks booleans are ints; ignore
print(maybe)

life = 3
if life > 0:    # this isn't a loop, so it is tedious and must be very repeated
    life -= 1   # += and -= are the same
if life > 0:
    life -= 1
if life > 0:
    life -= 1
if life > 0:
    life -= 1
elif life == 0:     # elif, not else if, and == is the same
    # use the word and instead of &&, and or instead of ||, and not instead of !=
    print("zero life")
else:
    print("whoops")
print(life)

# while loops are the same
lower_bound = 0
upper_bound = 5
for counter_variable in range(lower_bound, upper_bound):    # this is like (int x = 0; x<5; x++)
    print(counter_variable)


# continue skips code in the loop but continues to loop. break breaks the loop entirely
