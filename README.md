# Syntax

Spaces and tabs will be ignored  

### `(<operation>)`
Operations inside brackets will be performed at a higher priority than those outside  
- `1 + 2 * 3` will yield 7, but `(1 + 2) * 3` will yield 9  

Operational priority will remain the same inside the brackets  
- The expression `(1 + 2 * 3) * 2` will yield exactly the same result as `(2 * 3 + 1) * 2`

## Elementary Objects
### NUM
No keyword required  
Integer: Enter a number or a string of numbers with no spaces or commas, e.g (`1`, `123`, `5557`, `2000498`)  
Floating Point: Enter a number or a string of numbers followed by a ".", followed by a number or string of numbers, e.g. (`1.2`, `12345.678`)

#### Booleans
Represented as a NUM, false is 0 and anything else is true.

## Numerical Operations

### `<NUM>`
Returns the value given, e.g (`123` will yield 123)

### `-<NUM>`
Returns the negative of the NUM entered, e.g. (`-5` will yield -5)

### `<NUM> + <NUM>`
Adds two numbers together, e.g. (`2 + 2` will yield 4)

### `<NUM> - <NUM>`
Subtracts second number from the first, e.g. (`3 - 2` will yield 1)

### `<NUM> * <NUM>`
Multiplies two numbers together, e.g. (`2 * 3` will yield 6)

### `<NUM> / <NUM>`
Divides first number by the second, e.g. (`4 / 2` will yield 2, `5 / 2` will yield 2.5)

### `<NUM> ^ <NUM>`
Exponents first number by the second, e.g. (`2 ^ 3` will yield 8)

## Variables

### Built in variables
NULL = 0  
TRUE = 1  
FALSE = 0

### Assignation: `VAR name = operation`

Assigns a variable with a name of name, which can be made of letters, digits and underscores, where the first character must be a letter, to the result of the operation after the equals sign, which may be a pre-defined variable.  
e.g(`VAR a = 5`, sets a equal to 5. `VAR a = 5 * 5` sets a equal to 25. `VAR b = a` would then assign b to the value of a, 25)

Multiple variable assignation to one value may occur on one line, so long as the value to be assigned is last.  
e.g.(`VAR foo = VAR bar = 8` will set both foo and bar equal to 8)

Variable assignation may also occur inside an operation, so long as it is prioritised with brackets.  
e.g.(`6 / (VAR x = 6)` will return 1 and set x equal to 6)

### Access: `<name>`

Returns the value of the variable associated with &lt;name&gt;.  
e.g.(If foo is set to 12, `foo` will return 12)

May be used inside other expressions or operations to replace the elementary type it is associated with.  
e.g.(If bar is set to 13, `26 / bar` will return 2)

## Comparative Operations

These take a lower priority than their operations, therefore will compare the results of the operations on either side of them.

### `<OP> == <OP>`
Returns 1 if the operations are equal, returns 0 if not.

### `<OP> != <OP>`
Returns 1 if the operations are not equal, returns 0 if they are.

### `<OP> < <OP>`
Returns 1 if the first operation is less than the second operation.

### `<OP> > <OP>`
Returns 1 if the first operation is greater than the second operation.

### `<OP> <= <OP>`
Returns 1 if the first operation is less than or equal to the second operation.

### `<OP> >= <OP>`
Returns 1 if the first operation is greater than or equal to the second operation.

## Logical Operations

These take a lower priority than their operations, therefore will compare the results of the operations on either side of them.

### `NOT <OP>`
Returns 0 if OP is equal to 1, 0 otherwise.

### `<OP> AND <OP>`
Returns 0 if either of the operations are not equal to 1.

### `<OP> OR <OP>`
Returns 0 if both of the operations are not equal to 1.

## IF statement

If's take a lower priority than their operations, therefore will execute based on the results of their operations.

### `IF <comparison> THEN <operation>`
Executes &lt;operation&gt; if &lt;comparison&gt; is true.

### `IF <comparison> THEN <operation> ELIF <comparison2> THEN <operation>`
Will check in order of statements and execute respective &lt;operation&gt; if respective &lt;comparison&gt; is true.

### `IF <comparison> THEN <operation> ELSE <operation2>`
Executes &lt;operation2&gt; if &lt;comparison&gt; is false.

### `IF <comparison> THEN (IF <comparison2> THEN <operation>)`
Nested IF statements only work if prioritised with brackets.  
This is because if you tried `IF <comparison> THEN IF <comparison2> THEN <operation> ELSE <operation2>`, the ELSE is assigned to the inner loop, not the outer.
