# Type casting and data type conversion

str_num: str = "80"
print(str_num)
print(type(str_num))

str_num_to_int: int = int(str_num)
print(str_num_to_int)
print(type(str_num_to_int))

str_num_to_float: float = float(str_num)
print(str_num_to_float)
print(type(str_num_to_float))

# Falsy values
# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ""
# Empty range(0)
# int 0
# float 0
# complex 0j
# None
# False
str_num_to_bool: bool = bool(str_num)
print(str_num_to_bool)
print(type(str_num_to_bool))
