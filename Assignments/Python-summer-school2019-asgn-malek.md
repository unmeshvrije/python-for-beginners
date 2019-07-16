# 1. A Parrot
Write a program that prints whatever the user has entered.

* __Example output__:
```
Enter anything: anything
anything
```
> Extra assignment: The program keeps repeating words until the user enters “exit” then it stops.


# 2. Make it double
Write a program that takes a number as input and prints out the number times two.

* __Example output__:
```
Enter a number to double: 5
10
```

# 3. How long is it
Write a program that counts how many letters are there in an input string. Beware of counting “Punctuation Characters” like space, comma, period, question and exclamation marks. 

* __Example Output__:
```
Enter a string: Hello there!
10
```
> Extra assignment: The program also counts how many words are written. 


# 4. Consonants and Vowels
Write a program that counts how many vowels (a, e, i, o, u) and consonants are there in a word.

* __Output__: 

`<inputhas <numVowels> vowels and <numConst> constants.`

* __Example output__:
```
Enter a word: Beautiful
Beautiful has 5 vowels and 4 constants.
```
> Extra assignment: The program also can count consonants and vowels in a string. Beware of counting “Punctuation Characters” like space, comma, period, question and exclamation marks.


# 5. A welcome message
Write a program that asks the user for his name, country of birth, and field of study and then prints a welcome message: 

* __Output__:

`Hello <name>, I hope you had a nice travel from <land>. I am pretty sure that learning programming is useful in <field>.`

* __Example output__:
```
What is your name: John Doe
Where are you from: Mars
What do you study: Medicine
Hello John Doe, I hope you had a nice travel from Mars. I am pretty sure that learning programming is useful in Medicine.
```

# 6. Odd or Even
Write a program that asks the user to enter a number and then prints out if that number is odd or even:

* __Output__: 

`The Number <input> is <result>.`

* __Example output__:
```
Enter a number: 25
The number 25 is odd.
```
> Extra assignment: This program can tell if the input is divisible by 2 or not. Expand the program to tell if a 
number is divisible by 3 or 4 as well.


# 7. Simple Area Calculator
Write a program that calculates the area of a rectangle triangle or a circle.
Ask the user for the shape and based on it ask for the needed values to perform the operation. height and base for triangle, length and width for rectangle and radius for a circle.

* __Output__: 

`Area of this <shape> is <area>.`

* __Example output__:
```
Enter the shape’s name: triangle
Enter the height value: 6
Enter the base value: 9
Area of this triangle is 27.
```
> Note: you can use the math library for the value of pi. 

# 8. Temperature converter
Write a program that takes as an input a value with a unit (C for Celsius and F for Fahrenheit) and converts it to the other measurement unit.

* __Output__: 

`<inputTemp> is equal to <resultTemp>`


* __Example output__:
```
Enter a temperature value: 32F
32F is equal to 0C
```
> Note: 
> - T(°C) = (T(°F) - 32) / 1.8
> - T(°F)=T(°C)× 1.8 + 32


# 9.How many Years in this many Days 
Write a program that converts a number of days into years weeks and days.  

* __Output__:
 
`That is <years> years, <weeks> weeks and <days> days.`

* __Example output__:
```
Enter the number of days: 382
That is 1 years, 2 weeks and 3 days
```
> Extra assignment: Change the program and make it consider a leap year for every 4 years.


# 10. Squares Table
Write a program that helps students to memorize the square of numbers.
- Ask the user for a square of a random number.
- Check the input if it is correct or not and print a message with the result.
* __Example output__:
```
What is the square of 2: 6
Not correct, the square of 2 is 4. 
What is the square of 5: 25
Correct! Keep it up.
```
> Extra assignment: The program should randomly asks about either a square or square root to enhance the learning process. For * Example it asks about the square root of 16 and expects 4 as input.


# 11. Flow chart to code
Flow-charting has been used for a long time when designing algorithms and programs. Write a function according to the flowchart shown below.
[image]
The program should print the even numbers between 0 and max.
Test that program with some input.
* __Example output__:

```
Enter the a number: 9
0
2
4
6
8
```

# 12. Parents helping tool when buying games: 
Write a program that helps parents to choose a game for their kids and understand what the age labels of games mean, based on PEGI rating. 

- The user enters the age of the child
- The program prints what games fit this age based only on [PEGI age labels](https://pegi.info/what-do-the-labels-mean).
- The program also prints info about the type of content that might be expected in games with the highest fit age label.

* __Output__:
`According to PEGI, A player of the age <age> can play games with labels <labels>.`

`Games labeled with <highestLabel> contain <info>.`

* __Example output__:
```
Enter an age for a game advice: 14
According to PEGI, A player of the age 14 can play games with labels 12, 7 and 3.
Games labeled with 12 contain violence towards fictional characters and mild language.
```
> Note: Age labels and all info about them can be found [here](https://pegi.info/what-do-the-labels-mean). You can ignore “The PEGI content descriptors”.


# 13. Talking clock
Write a program that takes a digital time as an input and prints out a time in words.

* __Example output__:
```
Enter the time: 01:30 pm
It is half past one in the afternoon
```
> Note: consider only hh:00 or hh:30 minutes.

> Extra assignment: The program can detect and handle 24 hours format like “13:30”. 


# 14. Fibonacci sequence
write a program that prints the Fibonacci sequence from F(1) to F(n), while n is the user input value.
* __Example output__:
```
Enter a number: 6
1 1 2 3 5 8
```

# 15. Reversed Factorial
Write a program that finds the integer based on the result of its factorial
* __Output__:

`The number <inputis result of <num>!`

* __Example output__:
```
Enter a factorial of a number: 40320
The number 40320 is the result of 8!
```
> Extra assignment: Let the program report if the input is not a factorial of an integer. Then ask for a new input.

# 16. First and Last
Write a program that prints the first and the last weekday in your country. 
Create a tuple that contains the names of weekdays starting from the first day of the week in your country. 
Print the full tuple and a string that includes the first and last day of the week.

* __Output__: 

`The first weekday in my country is <firstand the last is <last>.` 

* __Example output__:
```
(‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’, ‘Sunday’, ‘Monday’)
The first weekday in my country is Tuesday and the last is Monday. 
```

# 17. The smallest and the biggest
Write a program that finds the smallest and the biggest number in a list.
Create a list of at least 6 random arranged numbers using `random` library function `randint(start, end)`.
Print the list and then print your results

* __Output__: 

`The smallest number is <smallest>`

`The biggest number is <largest>
`
* __Example output__:

```
[8, 4, 7, 6, 9, 1]
The smallest number is 1 
The biggest number is 9
```
> Extra assignment: The program also prints the range.


# 18. The Average
Write a program that calculates the average of a list of numbers.
Create a random list of at least 6 random arranged numbers using random library function randint(start, end).
print the list out and then print out the average.

* __Output__: 

`The average is <avg>`
* __Example output__:
```
[7, 2, 7, 9, 8, 3]
The average is 6
```
> Extra: The program also prints the mode of the list. In our case its 7.

http://pythontutor.com 
