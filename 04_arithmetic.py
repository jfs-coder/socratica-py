# Numbers: int, float, complex
# Operations: + - * /

x = 28 # int
y = 28.0 # float

print(f'converting int 28 to float: {float(28)}') # convert to float

print(f'converting float 3.14 to int: {int(3.14)}') # convert to int

# ints are narrower than floats
# floats are wider than ints

# simalarly any floats can be made into a complex number, but not vice-versa

tmp = 1.732 + 0j

print(tmp)

print(type(tmp))

print(f'convert float 1.732 to complex number: {complex(1.732)}') # convert to complex number

# cannot convert complex to float, you get a type error
# uncommenting the following line will display error: TypeError: can't convert complex to float
# print(f'converting complex to float: {float(1.732 + 0j)}')

# so, floats are narrower than complex numbers and complex numbers are wider than floats.


# ARITHMETIC OPERATIONS SECTION BEGINS





