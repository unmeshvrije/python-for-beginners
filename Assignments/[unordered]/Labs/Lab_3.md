# 1. Zipping Lists
Given two lists, zip them together and return the result.

* __Example:__
```
# Given [a, b, ..., z] and [0, 1, ..., 25] the program returns:
[a, 0, b, 1, ..., z, 25]
```

# 2. Age Differences
Given a list of (age, name) tuples, go through the list and for every adjacent pair (e.g. 0 and 1, 1 and 2, etc.) if the low-index age is older than the high-index age in the pair, print:
"{name-low-index} is {x} years older than {name-high-index}."

* __Example output:__
```
# Given the list [(16, Brian), (12, Lucy), (18, Harold)] the program prints:
Brian is 4 years older than Lucy.
```

# 3. Remove the Duplicates
Given a list of values, some of which are doubled, return an identical list, only without any duplicates.

* __Example:__
```
# Given the list [1, 1, 2, 3, 3] the program returns:
[1, 2, 3]
```

# 4. Only the Duplicates
Given two lists of values, with some values appearing in both lists, return a list containing only the shared values.

* __Example:__
```
# Given [1, 2, 3, 4] and [1, 4, 5, 6] the program returns:
[1, 4]
```

# 5. Count the Duplicates
Given a list of values, where some values are repeated a varying number of times, return a list of tuples that pair each (unique) value with the number of times it appeared in the original list. Make sure that you return the list of tuples in size order.

* __Example:__
```
# Given [1, 2, 2, 1, 4, 1, 3, 4] the program returns:
[(1, 3), (2, 2), (3, 1), (4, 2)]
```

# 6. Find the Largest Recombination
Given a list of numbers, output the largest possible number you can make from their recombination.

* __Example:__
```
# Given [10, 5, 16, 8] the program prints:
851610
```

# 7. Second Smallest
Take any number of integers as input to form a list and print the second smallest number in that list. If there is no second smallest number in the sequence, the program should print an error message and quit.
The program should read integers from user input to build the list and keep reading until a non-numeric value entered. Once a non-numeric input is detected, the program prints the second smallest value from the integers it has seen so far, then quits.

* __Example:__
```
Please enter the numbers for your list:
> 24 254 1 -5 -13 q
The second smallest number is: -5
```
```
Please enter the numbers for your list:
> 4 4 4 4 q
Error: There is no second smallest.
```

# 8. Calculator
Write a calculator that should be able to evaluate simple arithmetic expressions consisting of a number, an operator, and a number. The numbers should be from the set of real numbers, and the operators from the set of: (+, -, *, /).

The program should read and evaluate expressions until a character that is not a number is entered as the first value.

* __Example:__
```
Enter an expression:
> 2 + 3
The answer is 5.
Enter an expression:
> 2.3 * 4
The answer is 9.2
Enter an expression:
q
```

# 9. Rotating a Matrix
Rotate a square matrix 90 degrees clock-wise. (A matrix is a list of lists).

To make it harder, try rotating the matrix 'in-place' - this means that you rotate the matrix without creating a new one, only by editing the existing one.

* __Example:__
```
Given:
    01 02 03 04
    05 06 07 08
    09 10 11 12
    13 14 15 16

Output:
    13 09 05 01
    14 10 06 02
    15 11 07 03
    16 12 08 04
```




