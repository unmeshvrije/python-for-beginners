# 1. Generator
Write a generator that will provide the Fibonacci sequence for numbers below 100.

# 2. Iterable Class
Write an iterable class 'Range' that has the same functionality as Python's in-built `range` function. It should take three arguments, 'start', 'stop', and 'step'. The class should iterate using the `__next__` method and raise an exception when out of range occurs.

# 3. Decorator
1. Create a decorator function that can check zero division error.
2. Create a logging function that logs every decorated function into a file named by this function with the following format:

function_name.log:

Ran with arguments: arg1, arg2, arg3... and keyworded arguments: kwarg1, kwarg2, kwarg3...

In this assignment, you could use the logging model (import logging)
3. Create a timing decorator that prints out the running time of decorated functions.
4. Slightly modify the logging and timing decorators created in question 2 and 3 so that they can be chained together properly without losing information. (You may need to use the wraps decorator from the functools model.)
5. Assume you want to create a simple HTML web page. However, you only want to write the content do not want to repeatedly type all the tags yourself. Create a reusable decorator to generate HTML tags automatically for you and using it write the following html. (Ignore
the indentation)
```
<h1>Learning Python</h1>
    <h2>Chapter 1</h2>
    <h2>Chapter 2</h2>
        <h3>Section2.1</h3>
        <p></p>
    <h2>Chapter 3</h2>
```

# 4. Singly Linked List
A linked list is a data structure you can use to store dynamically changing data. The advantage of this data structure is that you can maintain a list of data and easily add and remove data from any arbitrary location in the list with a very low cost.

For example, with a traditional list, data is laid out in memory in a line. Take a look at the example string below:
```
Memory address: 0x0 0x1 0x2 0x3 0x4 0x5
Data:           "H" "e" "e" "l" "l" "o"
```
Clearly someone has misspelled "Hello", so we need to remove one of the 'e's. But how should we do that? We cannot just delete the second 'e', because what would remain in it's place? The number 0? 1? The letter "f"? Clearly nothing is appropriate - how would the computer know to skip the bad value?

What we need to do is move the other letters backwards in memory to remove one of the 'e's.
```
Memory address: 0x0 0x1 0x2 0x3 0x4 0x5
Data:           "H" "e" <-- "l" "l" "o"

Memory address: 0x0 0x1 0x2 0x3 0x4 0x5
Data:           "H" "e" "l" "l" "o"
```
However, notice that doing this requires us to make 3 moves of data. Imagine if we wanted to remove the second element in a list of length 1M, or 1B - those are very expensive moves.

(please note that the above example is simplified to show the concepts - this is not necessarily how strings work in reality)

Linked lists get around the array resizing problem by using 'nodes'. Nodes can point to each other allowing you to walk through the list node by node and just changing which node each node points to when you want to remove something. Take a look at the example below:
```
Head_node     Node_01       Node_02       Node_03
next_node --> next_node --> next_node --> next_node --> None
              some_data     some_data     some_data
```
You can think of each Node being a class (object) with a link to the next node (or None, if no next node exists) and the Head Node as a special Node that always exists to act as a starting point. Now if we want to remove, say, Node_02, we can just have Node_01 point to Node_03 and we're done    . Since we are no longer using a list (each Node will be in it's own location in memory) we don't need to resize or move anything, just change a value in Node_01 and our list is updated as needed.

Your task for today is to build a linked list and use it to keep track of some arbitrary data. You will need to create two classes, the first is the linked list itself (you can think of this as the head node - since it will always exist), and the second is the Nodes.

Your data structure should be similar to the skeleton laid out below. Feel free to change the structure if you find that easier, and you may add new functionality to the class if you like as well.
```
#-------------------------- Node Class --------------------------#
class Node:
    def __init__(self, data = None):
        self.data = data    # This can be anything: a string, number, object etc.
        self.next = None

#----------------------- Linked List Class -----------------------#
class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def print_list(self):
        # You will need to traverse the list here and print our the data of each node to the console. Feel free to format it how you like - but think about what information may be useful for someone to see if they were using your class.
        # Also, bear in mind that it may be easier to implement a 'print()' function in the Node and have this function call the print function on each node in the list.

    def add_node(self):
        # Think about the different ways might use this function - should they create the node themselves and pass it to this function (i.e. add_node(self, node)) or should they only give you data to create a node for them (i.e. add_node(self, data))?
        # Where should the new node be added? On the end - if so, is it worth keeping track of, not just the head node, but also the tail node?

    def clear(self):
        # This function should empty the whole list. Think about a sensible way to do this...you're reainitialising the list...do you already have code that does this?
```

As an extra challenge think about how you might implement functions to add and delete nodes in the middle of the list (the whole advantage of using a linked list in the first place!). This is a much harder problem to solve, so don't worry if you struggle with it at first - even if you don't manage to implement every function, you will still learn something, and you will find other problems easier in the future.

Good luck!