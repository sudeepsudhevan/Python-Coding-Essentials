# 1. Python Operators:
  * Python provides various operators for performing different operations on variables and values.
  * Here are some common operators:
    * Arithmetic Operators: Used for basic mathematical operations.
      * `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `//` (floor division), `%` (modulo), `**` (exponentiation).
    * Comparison Operators: Used to compare values.
      * `==` (equal), `!=` (not equal), `<` (less than), `>` (greater than), `<=` (less than or equal to), `>=` (greater than or equal to).
    * Logical Operators: Used to combine conditional statements.
      * `and`, `or`, `not`.
    * Assignment Operators: Used to assign values to variables.
      * `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`.
        
# 2. PEMDAS Rule (Order of Operations):
  * The PEMDAS rule helps determine the order in which mathematical operations are evaluated.
  * Let’s break it down:
    * P: Perform operations inside parentheses or groups first.
    * E: Evaluate any exponents.
    * MD: Perform multiplication and division from left to right.
    * AS: Finally, perform addition and subtraction from left to right.
    * Example:
 ```
      # Using PEMDAS rule
result = 10 - 7 // 2 * 3 + 1
# First: 7 // 2 = 3
# Second: 3 * 3 = 9
# Third: 10 - 9 + 1 = 2
print("Result using PEMDAS:", result)  # Output: 2

# Using parentheses to alter order
result_alternate = (10 - 7) // 2 * 3 + 1
# First: 10 - 7 = 3
# Second: 3 // 2 = 1
# Third: 1 * 3 = 3
# Fourth: 3 + 1 = 4
print("Result with parentheses:", result_alternate)  # Output: 4
```      
