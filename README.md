# Loops in Python Workshop 

## Duration:
Approximately 60 minutes.

## Objectives:
- Understand the concept behind the use of loops in computer programming.
- Distinguish the differences between for loops and while loops.
- Practice applying loops into Python-based coding exercises and projects.
- Recognize loop errors/bugs and apply debugging techniques to fix them.

## Materials (Needed For Teacher & Students):
- Access to computer & WiFi.
- Github Account.
- Replit Account OR an IDE with Python installed.
- **IF REMOTE, Zoom or Google Meet account.**

## Prerequisites: 
- Should have a solid foundation in the following topics in Python: Variables, Data Types (ex: ints & strings), Conditional Logic (with boolean/logical operators) & Lists.
- Should have some knowledge on some built-in Python functions and/or modules (ex: random, math & input).
- **IF USING IDE, should know the basics of Git when accessing and modifying files in the coding exercises (ex: committing, forking, push/pull requests).**

## Grade Level:
Recommended for high schoolers (9th-12th) with some basic knowledge on Python.

## Note On Participation:
> [!NOTE]
> There will be some questions, examples, and coding exercises throughout the lesson plan. You can optimize the content of these interaction pieces based on your classroom. It's highly recommended to go over the content of the interaction pieces as they help progress to the final project of the lesson.
> 
> When teaching remotely, specifically on Zoom, encourage students to use the 'Rasie Hand' feature and use break out rooms when you start doing coding exercises and the coding final mini-project.
> 
> You will see an (important sign) next to these pieces to encourage student participation during lecture for questions, peer coding and/or independent work.


## Introduction To The Concept of Loops:
- We'll start with some real life applications of loops to get the students comfortable with the idea behind them.
- Emphasize that a **loop** is an action that occurs over and over and over again.
> [!IMPORTANT]
> Discuss with the class an example of a morning routine (ask the class the first couple of things they do in the morning)
- This exercise is to prove that when you have a morning routine, it is vital it remains constant and turns into a pattern everyday.

- Display the class with a real life application of a loop (something that keeps running):
  - International Space Station that continuously orbits the Earth **([GIF](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonVisuals/ISSgif.gif)).**
      - Discuss with the class that the coordinates are always moving therefore the ISS has a job to orbit continuously.
      - [JSON file that tracks the longitude/latitude coordinates of the ISS](http://api.open-notify.org/iss-now.json?callback=CALLBACK)
      - [NASA website of spotting the ISS geographically](https://spotthestation.nasa.gov/)
> [!IMPORTANT]
> Ask the class for more real life applications that can relate to a loop, even if there's a stop to it eventually.
> 
> Examples can include a car running until it needs gas or a candle burning until the wick burns below the wax to help them out.

## Examples of Loops in Coding:
- Explain the two pictures and the pseudo code that accompany with each (IKEA website & Flappy Bird GIF). This is a way to show off how loops are typically integrated in coding applications such as shopping websites, phone applications and video games:
  
[IKEA Website Example](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonVisuals/ikeaChairs.png)
- For the following IKEA example, we see that there are 3 chairs being displayed.
- With the assistance of loops, they can iterate through any type of search result and display the following format.
```
# pseudocode for IKEA chair picture

for every chair in IKEA website:
	display picture of chair
	show name of chair
	type of furniture
	display price or price on sale
	arrange star ratings and number of reviews
```

[Flappy Bird Example:](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonVisuals/flappyBird.gif)

> [!IMPORTANT]
> Before you show off the pseudocode of the Flappy Bird GIF, ask the class what specific actions are being looped throughout the game
> If it helps, give them this example and ask them to fill in the blanks

```
while flappy bird starts:
	move background of trees/skyline
	__________________
	if the bird goes through a pipe:
		_________________
	else:
		_________________


for every _________ in gameplay:
	bird fly/jump action
```
### Solution:
```
while flappy bird starts:
	move background of trees/skyline
	spawn new pipe with random opening
	if the bird goes through a pipe:
		update score to add 1 point
	else:
		lose game and display end screen


for every key pressed/tapped in gameplay:
	bird fly/jump action

```


## For Loops:
- Start to explain that there are 2 ways of looping in Python, the first one we'll be learning are **for loops**.
- [A GIF of Bart Simpson writing "HAVE A GREAT SUMMER, EVERYONE" on the board over and over again](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonVisuals/bartWriting.gif)
- Show off a GIF and explain how long it would take to write that specific statement 10 times, 100 times or even a million times.
- Emphasize it would be would be very difficult to do manually and show off this example to show off this point with the following code:
  
```python
print("HAVE A GREAT SUMMER, EVERYONE")
print("HAVE A GREAT SUMMER, EVERYONE")
print("HAVE A GREAT SUMMER, EVERYONE")
print("HAVE A GREAT SUMMER, EVERYONE")

# ...after many more print statements..

print("HAVE A GREAT SUMMER, EVERYONE")
```
- The solution to that is to write out for loop knowing the amount of times we want to print this statement out
- If we wanted to print "HAVE A GREAT SUMMER" 5 times using a loop, we'll write out the following:

```python

for i in range(5):
  print("HAVE A GREAT SUMMER, EVERYONE")

```

- Explain to the class which solution looks easier to write out in terms of how concise and minimal it is which can save a lot of time for coders.

## Syntax:
- The major case when using for loops is that we will know in advance how many times the loop will need to iterate through a collection.
- When we talk about collections, we are referring to some sort of data that we can extract from (examples include elements in lists or characters in strings).
- Iteration is a repeated performance where it executes the same set of instructions a given number of times or until a specified result is obtained.

Syntax:
```
for <temp variable> in <collection>:
  <executable code>
```

Break down each component to the following use case and/or definition:

- _**for**_ keyword = indicates the start of a for loop.
- _**temp variable**_ (temporary variable) = used to track the value of the element in the collection the loop is currently on. The temporary variable can be any name you'd like it to be but it's always encouraged to make a temp variable that relates to what you're doing.
- _**in**_ keyword = separates the temp variable from the collection used for iteration.
- _**collection**_ = the content that we're looping over with a colon afterwards.
- _**executable code**_ = the action to perform on each iteration of the loop.

Example:
```python
speech = ["Spanish", "French", "Italian", "English"]

for languages in speech:
  print(languages)

# Output:

Spanish
French
Italian
English
```
> [!IMPORTANT]
> Ask the class the following questions:
>
> What type of collection are we using for this loop that will be printed out here?
>
> What temp variable is being used in this example?
>
> What will the output be?

```python
for word in "hello":
  print(word)

#
#
#
#
#
#
#
#
#
#
#
#


# Solution:

# The collection we're using is a String that is going to print out individual character

# Output from the loop:
h
e
l
l
o

```

## Loops in Ranges:
- The same way we want to perform an action a certain amount of times in loops, it becomes most helpful when it comes to numbers.
- When we're not dealing with collections, we can iterate over a range of integers that exist.

Example #1: 
- Let's say we want to print out a range of numbers from 0 through 5.
- We will be using a temporary variable inside of a range and using the parenthesis after it to control the amount of times.
- The reason why we use 6 instead of 5 is because that number is exclusive from that endpoint.


```python
for i in range(6):
  print(i)

 # Output:
0
1
2
3
4
5
```

Example #2: 
- We want to start off from a different number instead of zero.
- In order to start off with a non-zero number, we'll need two numbers in the range (the min and max).
- Let's use an example where we go from 10 through 15.

```python
for j in range(10,16):
  print(j)

# Output:
10
11
12
13
14
15
```

Example #3:
- Now that we know how to print out values from the min and max, let's now print out a pattern from the range.
- This will know require 3 numbers in the range that goes like this: `for k in range(start, stop, step)`
- With the following syntax, let's print out multiple of 5's between 50 through 75.

```python
for k in range(50, 76, 5):
  print(k)

# Output:
50
55
60
65
70
75
```
> [!IMPORTANT]
> Let students either use [Replit](https://replit.com/) and copy the following patterns and Invite you to their project link
>
> OR
>
> [Fork this file](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonExercises/pythonLoopEx1.py) from the repo and create a pull request with your name and class name.
> 
> Let's try getting the class to print out the following numerical patterns using for loops:
>
> Be mindful that the patterns will be displayed horizontally but the output must be printed vertically with the commas represented as a new line for the value.
> 
> The 3 ellipses are filler to save space but the values must be printed out in between as well.
> 
> [Solutions will be in the following link](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonSolutions/pythonLoopSol1.py)

### Coding Exercise #1:
```python
# Pattern 1:
# 21, 25, 29, ... 97
########### CODE BELOW HERE #########




# Pattern 2:
# -4, -2, 0, ... 3
########### CODE BELOW HERE #########






# Pattern 3:
# 3 mississippi, 2 mississippi, 1 mississippi
########### CODE BELOW HERE #########







# Pattern 4:
# Create a list of 5 emojis of your choice and print them using a for loop
# 😬😎😁👽🥳
########### CODE BELOW HERE #########








```
## While Loops
- Compared to for loops, while loops serve a similar purpose of repeating an action.
- The difference is that it will continue as long as the given condition is true.
- The following is the syntax of a while loop written in Python:

```
while <condition>:
  <executable code>
```
- The condition is typically a boolean expression that expresses if it is either true or false.
- If the condition isn't true during the while loop, the code is finally finished.
- NOTE: Anything you can output with a for loop, you can use a while loop for the solution as well. Something to keep in mind is that you have to choose which loop fits better in what specific scenario.

While Loop Example:
- Let's say we want to print out the number 1 through 5 using a while loop.
- What we have to do first is we should create a variable called 'count' and assign it to 1. This will help have something to compare to in the condition.
- As long as the count variable is less than or equal to 5, we will add 1 to the count and continue to print the number until we reach 5.

```python
count = 1

while count <= 5:
  print(count)
  count = count + 1

# Output:
1
2
3
4
5

```

## Breaks In Loops:
- This keyword helps terminate the current loop and continues the execution to the next statement.
- The word 'break' can help us with stopping a loop when we finally found an element or satisfies a condition that doesn't require the rest of the loop to be finished.

Example:
- Let's say we're given a list of numbers and our goal is to iterate the list of numbers but break the loop when we encounter an even number.

> [!IMPORTANT]
> Ask the class the fill in the blank on how we can detect an even number in Python
> If the class isn't sure, provide a hint of using the modulo operation

```python

numbers = [3, 55, 9, -21, 50, 6]

for num in numbers:
  if (____________):
    print("Even number detected!")
    break
  print("Odd number passed", num)

```

Solution:
```python
numbers = [3, 55, 9, -21, 50, 6]

for num in numbers:
  if (num % 2 == 0):
    print("Even number detected!")
    break
  print("Odd number passed", num)



# Output:
Odd number passed 3
Odd number passed 55
Odd number passed 9
Odd number passed -21
Even numbers detected!

```

> [!IMPORTANT]
> Let students either use [Replit](https://replit.com/) and copy the following patterns and Invite you to their project link
>
> OR
>
> [Fork this file](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonExercises/pythonLoopEx2.py) from the repo and create a pull request with your name and class name.
> Follow the comments and use what you learn about while loops to produce the following results:
>
> [Solutions will be in the following link](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonSolutions/pythonLoopSol2.py)
> 
### Coding Exercise #2:
```python
# First Coding Session:
# Output the following values using a while loop: 9,8,7,6,5
########### CODE BELOW HERE #########














# Second Coding Session:
# Create a list of ingredients you'd use to make a cake (minimum of 4 elements)
# As you iterate through the list, print out "We have that ingredient!"
# If you come across the ingredients of either flour or sugar, print out the statement "Wait, we don't have that!" and use the keyword break
#
# Complete this challenge with a for loop. If you have more time, try creating a while loop solution as a bonus!
########### CODE BELOW HERE #########


















```
## Infinite Loop:
- The last important concept is something you may have came across while coding
- Let's say the condition you have written is always true; this means that your executable code is constantly running!

> [!IMPORTANT]
> Ask the class what type of expression can you insert in the blanks that will create an infinite loop.
> If they have an answer, compare and explain why it works out as an infinite loop.

```python
count = 5

while count _ __:
  print("repeat")




# One Example of a Solution
count = 5

while count < 10:
  print(count)

# Since 5 will always be less than 10, the count will continue to print until we stop the code.
# This is the example of an infinte loop.
# If you increment the count variable after every iteration, then it'll stop until the condition turns false.

```


> [!IMPORTANT]
> Let students either use [Replit](https://replit.com/) and copy the following patterns and Invite you to their project link
>
> OR
>
> [Fork this file](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonExercises/pythonFinalEx.py) from the repo and create a pull request with your name and class name.
> 
> Explain the instructions carefully and students may work together if they'd like
> Encourage students to look up Python documentation if needed (ex: GeeksForGeeks, StackOverflow, etc...)
>
> > [Solutions will be in the following link](https://github.com/JaiTheGuy/GMPythonLoops/blob/main/loopsPythonSolutions/pythonFinalSol.py)

### Final Project: Number Guessing Game
``` python
# Goal: Create a game where you keep guessing a number until you get it right!
# Step 1: Create a variable that holds onto a random number based on your preferred range (hint: you might need to import!).
# Step 2: Make a while loop where the condition is 'True'.
# Step 3: Have the user guess the number and each time they guess incorrectly, have a print statement that tells them to keep guessing.
# Step 4: If they guess the number correctly, use a print statement to congratulate them and then break from the loop.

# BONUS:
#1: Tell the user if their guess is higher or lower after each turn.
#2: Tell the user how many turns it took them to get the answer right when they win.
#3:  If someone enters something that's not a number or a number out of the range, have a condition that prints out an error message for that turn and ask them to try again.

########### CODE BELOW HERE #########












```
## Conclusion/Review Questions:
- At the end of this lesson, the students should be more familiar with the practices of loops and should be able to implement them in their future projects when needed.

> [!IMPORTANT]
> Review Questions:
>
> What is the difference between a for loop and a while loop?
>
> What causes an infinite loop?
>
> When printing out a for loop in a range, what would the 3 numbers in the parenthesis represent?


> [!NOTE]
> These are the ideal time allocations you'd need to time exactly how long each subject & exercises should be in a 60 minute workshop.
- Introduction To Loops: 5 minutes
- For Loops: 8 minutes
- Syntax of For Loops: 5 minutes
- Coding Exercise #1: 8 minutes
- While Loops: 6 minutes
- Breaks In Loops: 3 minutes
- Coding Exercise #2: 6 minutes
- Infinte Loop: 3 minutes
- Final Project: 9 minutes
- Conclusion: 2 minutes


