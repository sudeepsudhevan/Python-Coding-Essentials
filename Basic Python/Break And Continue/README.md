# `break` And `continue` in Python

* ##`break` Statement:##
  * The break statement is used to terminate a loop immediately when a certain condition is met.
  * It is commonly used inside loops (such as for or while) to exit the loop prematurely.
  * Example using for loop:
  ```
  for i in range(5):
      if i == 3:
          break
      print(i)
  # Output: 0 1 2
  ```
  * the loop terminates when i equals 3.

* ##`continue` Statement:##
  * The continue statement skips the current iteration of a loop and proceeds to the next one.
  * It allows you to omit specific iterations based on a condition.
  * Example using for loop:

  ```
  for i in range(5):
      if i == 3:
          continue
      print(i)
  # Output: 0 1 2 4
  ```
  * the loop skips the iteration when i is equal to 3.
