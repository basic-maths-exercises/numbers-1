# Introduction to natural numbers

Now that you have learned how to write basic computer programs, we can use Python to explore some of the mathematical ideas that you have encountered during your undergraduate course.  In this series of exercises, we are going to consider numbers in more detail and tackle a rather tricky notion; namely, that there are multiple ways to represent numbers.  It is thus wrong to think of the number three thousand two hundred and sixty as merely 3260. We can also express this number as 110010111100 or even as CBC.  This previous sentence is not a form of madness. In these second two cases, we are just using less conventional methods to represent the number.    

Let's start the business of understanding these other representations of numbers by understanding how the familiar representation 3260 works.  As you are no doubt aware when we write 3260 we are stating that the number we are interested in is constructed as follows:

1. First, multiply three by one thousand.
2. Next, multiply two by one hundred.
3. Next, multiply six by ten.
4. Next, multiply one by zero.
5. The number we are interested in is the sum of the four numbers that you obtained from these four multiplications.

__To complete this exercise, I would like you to use this idea to complete the function called `numberOfThousands` shown in `main.py`.__  This function should take an integer with a value less than or equal to 9999, which we shall call `N` as input.  The function should then return the first-digit of that number, i.e. if 3260 is input the function should return 3.  You will likely need to use the `np.floor` function to complete this task.  This function chops off the part of the number after the decimal point.  In other words, if we do:

````
a = np.floor( 3.260 )
````

then the variable `a` will be set equal to 3. 
