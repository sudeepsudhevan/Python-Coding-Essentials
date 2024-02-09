# Naming Conventions in Python:
  * Python follows a set of guidelines established in PEP8, the official style guide. While these conventions are not enforced by the Python interpreter, adhering to them is considered good coding practice.
  * Here are the fundamental rules for naming variables, functions, classes, and other identifiers:
    * Names are case-sensitive.
    * Names cannot start with a digit.
    * Names can contain letters, numbers, and underscores.
  * Let’s explore different naming styles:
    * Snake Case: All words are in lowercase, separated by underscores. Used for function and variable names.
      * Example: `user_name`, `my_function`
    * Pascal Case: Similar to camel case but starts with a capital letter. Used for class names.
      * Example: `ClassName`, `MyClass`
    * Camel Case: First letter of each word capitalized except for the first word. Not commonly used in Python.
      * Example: `myVariable`, `isInstance`
    * Upper Case with Underscores: Used for constants.
      * Example: `PI`, `MAX_OVERFLOW`

  ![image](https://github.com/sudeepsudhevan/Python-Problems/assets/31392327/e3b27397-aae1-4418-861a-21a04625f182)

# Handling Variable Naming Errors:
 * If you encounter a NameError, it means you’re trying to use a variable that isn’t defined yet. For example:
   ```
   print(x)  # NameError: name 'x' is not defined
   ```
 * To fix this, define the variable before using it:
   ```
   x = 5
   print(x)  # Output: 5
   ```   

