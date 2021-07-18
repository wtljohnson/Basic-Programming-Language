# Basic Maths Interpreter

Simple maths interpreter that uses BIDMAS

# Syntax

Spaces and tabs will be ignored

## Elementary Objects
### NUM
No keyword required  
Integer: Enter a number or a string of numbers with no spaces or commas, e.g (1, 123, 5557, 2000498)  
Floating Point: Enter a number or a string of numbers followed by a ".", followed by a number or string of numbers, e.g. (1.2, 12345.678)

## Operations
### NUM + NUM
Adds two numbers together, e.g. (2 + 2 will yield 4)

### NUM - NUM
Subtracts second number from the first, e.g. (3 - 2 will yield 1)

### NUM * NUM
Multiplies two numbers together, e.g. (2 * 3 will yield 6)

### NUM / NUM
Divides first number by the second, e.g. (4 / 2 will yield 2, 5 / 2 will yield 2.5)

### NUM ^ NUM
Exponents first number by the second, e.g. (2 ^ 3 will yield 8)

## Expressions
### (Operation)
Operations inside brackets will be performed at a higher priority than those outside, e.g (1 + 2 * 3 will yield 7, but (1 + 2) * 3 will yield 9)  
Operational priority will remain the same inside the brackets, i.e (The expression (1 + 2 * 3) * 2 will yield exactly the same result as (2 * 3 + 1) * 2)

### VAR
Assignation: VAR name = operation  
Assigns a variable with a name of name, which can be made of letters, digits and underscores, where the first character must be a letter, to the result of the operation after the equals sign, which may be a pre-defined variable.  
e.g(VAR a = 5, sets a equal to 5. VAR a = 5 * 5 sets a equal to 25. VAR b = a would then assign b to the value of a, 25)

Multiple variable assignation to one value may occur on one line, so long as the value to be assigned is last.  
e.g.(VAR foo = VAR bar = 8 will set both foo and bar equal to 8)

Variable assignation may also occur inside an operation, so long as it is prioritised with brackets.  
e.g.(6 / (VAR x = 6) will return 1 and set x equal to 6)

Access: name
Returns the value of the variable associated with name.  
e.g.(If foo is set to 12, foo will return 12)

May be used inside other expressions or operations to replace the elementary type it is associated with.  
e.g.(If bar is set to 13, 26 / bar will return 2)
