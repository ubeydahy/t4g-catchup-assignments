#Part 3 -- Integers, Floats & Arithmetic
#Task 1 : Declaring integer and float variables
#Integer variable
num1 = 20
num2 = 5

#Float variable
float1 = 5.0
float2 = 5.5

#Addition
print(num1 + num2)

#Subtraction
print(num1 - num2)

#multiplication
print(num1 * num2)

#division
print(num1 / num2)

#floor division
print(num1 // num2)

#modulo
print(num1 % num2)

#exponential
print(num1 ** num2)

#Task 2 : Area and perimeter of a rectangle
length = 8
width = 4

area = length * width
perimeter = 2 * (length + width)
print(f"A rectangle with length {length} and width {width} has an area of {area} and a perimeter of {perimeter}")

#Task 3 : Type conversion
#Integer to float
integer_value = 5
convert_to_float = float(integer_value)
print(convert_to_float)

#Float to integer
float_value = 7.9
convert_to_integer = int(float_value)
print(convert_to_integer)

#Data type
print(type(integer_value))
print(type(float_value))
print(type(convert_to_float))
print(type(convert_to_integer))