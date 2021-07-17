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
