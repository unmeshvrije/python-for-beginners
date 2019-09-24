# 1. Run-Length Encoding
Write a program that implements a simple form of run-length encoding. The program should take a string as input, and check that the characters in the string are from 'a' to 'z'. You can assume that any other inputs are invalid. The output should be in the form of &lt;number&gt;&lt;character&gt; repeated for each consecutive sequence of characters.

* __Example:__
```
# Given: "aaeeeaae" the program returns:
"2a3e2a1e"

# Given: "rr44eArrre" the program returns:
"Invalid Input"

# Given: "eeeeeeeeeeeeeeee" the program returns:
"16e"
```

For extra practice, have the program store the numbers and characters in separate lists and have it take the correct values from both when returning the answer.

# 2. Weave
Given two lists of numbers, weave them together into a single series by interlacing the numbers from each sequentially. You can assume that both lists will be the same length.

* __Example:__
```
# Given: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] return:
[1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]
```

For extra practice, think about who you should deal with input of different lengths? There is no "right" answer for this, but many options - throw an exception, only weave up to the length of the shortest, use default values to weave the full length, concatenate the extra length onto the end of the weave, etc.

# 3. Weave 2.0
This time write a Number_Row class that maintains a list of numbers. Give this class a method `weave` that interlaces any new lists into the internal list.

* __Example:__
```
Initial list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
First input:  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
First result: [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]

Second input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Second result: [1, 1, 10, 2, 2, 3, 9, 4, 3, 5, 8, 6, 4, 7, 7, 8, 5, 9, 6, 10, 6, 11, 5, 12, 7, 13, 4, 14, 8, 15, 3, 16, 9, 17, 2, 18, 10, 19, 1, 20]
```

For extra practice, think about how people might want to use this class - is there any extra functionality you might think would be useful? How should the class be instantiated - should the user have a list already, or can the first list be empty? What checks should you do with user input, etc.

# 4. Body Mass Index
Professor Hatzelklatzer has been researching the exceedingly rare Hatzelklatzer syndrome. The research shows that the syndrome is more likely to affect people who have high BMIs. BMI is a measure of weight in relation to height, and is defined as: weight/(height^2) and carries the units kg/m2. The World-Health Organisation (WHO) considers BMIs between 18.5 and 25 as ideal, and anything outside of these ranges as unhealthy.

Patient data is stored as strings in the following format:

"first_name last_name gender height_in_m weight_in_kg"

e.g. "Dean Johnson M 1.78 83", "Sophia Miller F 1.69 60"

Your program should take these strings as input and create a data structure (a class) to store information on each patient. The data structure for each patient should also make several useful methods available to enable easy access to information, to allowing printing in the following format: appropriate form of address, last name, the patient's BMI, and a statement of whether the patient is healthy, unhealthy or at risk of Hatzelklatzer syndrome as appropriate.

* __Example:__
```
"Mr. Johnson's BMI is 26.2 and he is at risk."
"Ms. Miller's BMI is 21.0 and she is healthy."
"Mr. McCulloch's BMI is 17.9 and he is unhealthy."
```

# 5. Body Mass Index 2.0
Professor Hatzelklatzer liked the previous program, but has realised that the output is not particularly useful for analysis. Instead, they would like the program to take a set of patient details as input, and output some analytical details.

The patient details will now include an indication as to the presence of Hatzelklatzer syndrome (P = positive, N = negative) and the patient details will be delivered as a list of strings.

* __Example:__
```
["Dean Johnson M 1.78 83 P", "Sophia Miller F 1.69 60 N", ...]
```

The program should read the data for all provided patients, calculate the average BMI and count the number of patients above and below this number with Hatzelklatzer syndrome, outputting the results as follows:

* __Example:__
```
The average BMI of the test subjects is x.
There are y cases of HK syndrome amongst people with BMI >= x.
There are z cases of HK syndrome amongst people with BMI < x.
```

For extra practice write a txt file that has different patient details on each line, and have your program take this file as input. Think about what simple errors might crop up, and how you can go about fixing or avoiding some of them.