# 1. Printing and user input v2
Modify the program you wrote yesterday so it can generate the following conversation:

* __Example output__:
```
He. What is your name: Emily
Hello, Emily. My name is Robert. How old are you: 23
I am 25 years old, so I am 2 years older than you.
```
# 2. A Bookstore
Suppose the cover price of a book is 24.95 EUR, but bookstores get a 40 percent discount. Shipping
costs 3 EUR for the first copy and 75 cents for each additional copy. User input is total number of
books and output is total cost of books. Use variables with clear names for your calculations and
print the result using a full sentence.
* __Example output__:
``` 
Enter the number of books: 
The cost of <> books is <> Euro's
```

# 3. Odd or Even
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


# 4. Parcel Delivery
The required postage for an international parcel delivery service is calculated based on item weight
and country of destination:

| Tariff zone | 0-2 kg | 2-5 kg | 5-10 kg | 
|-------------|--------|--------|---------|
| Europe      | 13.00  | 19.50  | 25.00   |
| World       | 24.50  | 34.30  | 58.30   |

Create two variables weight and zone and get their values using input. Use (nested) if-statements to find the postage cost based on these variables. Assign the result to a variable postage and print the result.

* __Example output__:
``` 
Enter destination: world
Enter weight: 4
The cost is 34.30 euro's
```

# 5. Simple Area Calculator
Write a program that calculates the area of a rectangle, triangle or a circle.
Ask the user for the shape and based on it ask for the needed values to perform the operation. height and base for a triangle, length and width for a rectangle and radius for a circle.

* __Output__: 

`Area of this <shape> is <area>.`

* __Example output__:
```
Enter the shape’s name: triangle
Enter the height value: 6
Enter the base value: 9
Area of this triangle is 27.
```
> Note: consider pi to be 3.14 or you can use the `math` library for the value of pi.

# 6. Flow chart to code
Flow-charting has been used for a long time when designing algorithms and programs. Write a function according to the flowchart shown below.

![flowchart image](https://github.com/unmeshvrije/python-summer-school/blob/master/Assignments/flowchart.png?raw=true)

The program should print the even numbers between 0 and max.
Test that program with some input.
* __Example output__:

```
Enter a number: 9
0
2
4
6
8
```
# 7. Squares Table
Write a program that helps students to memorize the square of numbers.
- Ask the user for a square of a random number.
- Check the input if it is correct or not.
- If the answer was not correct, give the user at least 3 chances to answer before printing the correct answer.
- The program keeps producing questions until the user enters `q` or `Exit`.
* __Example output__:
```
What is the square of 2: 6
Not correct. 
What is the square of 2: 4
Correct! Keep it up.
What is the square of 5: 25
Correct! Keep it up.
```
> Extra assignment: The program should randomly asks about either a square or square root to enhance the learning process. For * Example it asks about the square root of 16 and expects 4 as input.

# 8. Parents helping tool when buying games: 
Write a program that helps parents to choose a game for their kids and understand what the age labels of games mean, based on PEGI rating. 

- The user enters the age of the child
- The program prints what games fit this age based only on [PEGI age labels](https://pegi.info/what-do-the-labels-mean).
- The program also prints info about the type of content that might be expected in games with the highest fit age label.

* __Output__:
`According to PEGI, A player of the age <age> can play games with labels <labels>.`

`Games labeled with <highestLabel> contain <info>.`

* __Example output__:
```
Enter age for a game advice: 14
According to PEGI, A player of the age 14 can play games with labels 12, 7 and 3.
Games labeled with 12 contain violence towards fictional characters and mild language.
```
> Note: Age labels and all info about them can be found [here](https://pegi.info/what-do-the-labels-mean). You can ignore “The PEGI content descriptors”.
