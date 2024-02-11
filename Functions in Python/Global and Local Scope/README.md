# Global and Local scope

## Local Scope:
  * A variable created inside a function belongs to the local scope of that function.
  * It can only be used within that function
    ```
    def myfunc():
        x = 300
        print(x)
    
    myfunc()  # Output: 300
    ```

## Global Scope:
  * A variable created in the main body of the Python code is a global variable.
  * It belongs to the global scope and is available from within any scope (both global and local).
    ```
    x = 300
    
    def myfunc():
        print(x)
    
    myfunc()  # Output: 300
    print(x)  # Output: 300    
    ```
  * Global variables are accessible throughout the entire program.

## Global Keyword:
  * To create a global variable within a local scope, use the global keyword.
  * This allows you to modify a global variable from within a function.
    ```
    def myfunc():
        global x
        x = 300
    
    myfunc()
    print(x)  # Output: 300
    ```
  * Use the `global` keyword when you need to work with global variables inside a function.  
 The local scope takes precedence over the global scope, but you can explicitly access global variables using the global keyword when necessary
    
          
