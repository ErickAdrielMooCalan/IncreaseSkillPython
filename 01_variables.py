# How to name variables
firstname = "Erick"
print(firstname)

my_variable_string = "Hi I'm a variable"
print(my_variable_string)

_if = "This is a variable not IF"
print(_if)

my_int_variable = 27
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)


# String concatenation
print(my_variable_string, my_int_variable, my_bool_variable)
print("Hi, I'm ", firstname)

# Convert integer to string
result = str(my_int_variable)
print(result)
print(type(result))


# System functions (count the number of characters)
print(len(my_variable_string))


# Variables on a single line
secound_name, last_name, alias, age = "Adriel", "Moo", "MooXee09", 22
print("My name is:", secound_name, last_name, ", my alias is: ", alias, "and en my age is: ", age)