# 1. Palindrome 1.0
Write a program that will print the following string:

"abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba"

Do this without hard-coding any values (try printing with a loop).

# 2. Palindrome 2.0
Copy your code from Palindrome 1.0 and extend it to include the following functionality:
* Read a single letter from standard input
* Return the palindrome from 'a' to the input letter

* __Example:__
```
# Given an input letter of 'c', the output should be:
"abcba"

# Given an input letter of 'f', the output should be:
"abcdefedcba"
```

# 3. Palindrome 3.0 - Pyramid
Write a program that prints the following pyramid:
```
              a
             aba
            abcba
           abcdcba
          abcdedcba
         abcdefedbca
        abcdefgfedcba
       abcdefghgfedcba
      abcdefghihgfedcba
     abcdefghijihgfedcba
    abcdefghijkjihgfedcba
   abcdefghijklkjihgfedcba
  abcdefghijklmlkjihgfedcba
 abcdefghijklmnmlkjihgfedcba
abcdefghijklmnonmlkjihgfedcba
```
The pyramid should be 15 levels high. For extra work, consider changing the functions you used so that the user can specify a certain indent (e.g. allow the user to print the pyramid in the centre of their screen if they provide your function with their screen-width).

# 4. Collatz Conjecture
One of the most renowned, unsolved maths problems is the Collatz Conjecture. The conjecture is probably correct but, despite its apparent simplicity, no mathematical proof has been found since its original proposal in 1937. Using computers, all numbers up to 10,258 have been found to fulfil the conjecture. Your job is to write a program that takes a number as input, and prints out that number's Collatz sequence.

For extra practice:

* Try using both the modulo (`%`) operator to test for evenness, and the bit-wise AND operator (`&`).

* Try writing your function both using a for-loop as well as recursively.