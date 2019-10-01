#!/usr/bin/env python
# coding: utf-8

# # Python 3 Introductory Workshop

# ### Topics
#     - Why Python?
#     - Variables
#     - Operators
#     - Collections
#     - Conditionals
#     - Loops

# ### Why Python?
# Python is known for being one of the most versitile and easy to use languages
#     
#     - Simple syntax makes it easy to learn
#     - Easy and intuitive to read, even with minimal programming knowledge
#     - Great for prototyping and quickly writing working code
#     - Portable across systems; As long as Python is installed it will run on any operting system
#     
# Popular uses for Python include
# 
#     - Mathematics and big data
#         Packagages used for reading in, manipulating, and analyzing data quickly(Numpy, Pandas)
#     - Simple Scripting
#         Writing a functional program that performs an individual task (rasberry pi)
#     - Server side web development (django, flask)
#         Server side scripting means hosting a web server that can handle requests
#     - Software development
#         Python is robust enough to handle creating almost anything you want to do

# ### Variables

# We need to be able to remember information for later, to do this we use variables.
# we can assign a variable a value with =
# 
# Here, we're going to look at 4 variable types:
#     
#     -integers
#     -floats
#     -strings
#     -booleans
# 
# Python is a "dynamically typed language"
# 
# This means that we do not need to declare variable types, or tell the computer what type they are, we just trust Python to keep track for us.

# ##### Integers
# 
# integers; positive or negative numbers WITHOUT decimal places - the same as in math

# In[5]:


a_int = 6
print(a_int)


# #### Floats
# floating point numbers; numbers WITH decimal places
# in actuality, floats are only approximations of numbers, so sometimes (as we'll see later) they can get a little weird
# If you're interested in more info on why this occurs, go to this link: https://docs.python.org/3/tutorial/floatingpoint.html

# In[6]:


a_float = 6.6
print(a_float)


# ##### Strings
# sequence of characters surrounded by "" or ''

# In[7]:


a_string = "hello"
b_string = "17"
# Double quoted strings ("") can have single quotes ('') in them
# Single quoted strings can have double quotes in them
c_string = 'This is a pair of of "double quotes" in a string.'


# we can access strings with [ ] with 0 being the first character and -1 being the last.
# [:] will also give us a range of characters 

# In[8]:


print(a_string[0])
print(a_string[-1])
print(a_string[1:4]) #this will return the 3 characters including character 1 but not character 4 


# ##### Booleans
# True / False values with the first letter capitalized

# In[9]:


a_bool = True # any non-zero number as a boolean will be cast to True
b_bool = False # 0 will be cast to False


# If we want to make a variable but have nothing in it, not even the value 0, we use None. This gets helpful in some more advanced programs, but for the basics, just know it exists. 
# It is a useful thing to check when passing variables to different functions to ensure that input is correct. You always want to check that your input is not None and that it is not outside the bounds of what you need it to be for that function to ensure that someone can't break your code. 

# In[10]:


a_var = None


# If we want to see the value stored in a variable, we can use the built-in print( ) function.
# Print will show us whatever is inside the ( ) to our console, for Jupyter, the console will appear below our code blocks
# 
# and if we want to know the type of a variable, we can use the type( ) function

# In[11]:


print(type(a_int))
print(type(a_float))
print(type(a_string))
print(type(a_bool))
print(type(a_var))


# You can name a variable almost anything you want with just a few rules
# 
#     - can't start a variable name with numbers
#     - can't have a space in a variable name
#     
# You should generally follow a few guidelines as well
# 
#     - start a variable name with a lowercase letter
#     - keep them descriptive

# ### Operators

# Operators let us do things with variables and values, we've already seen one: =
# 
# The basic operators to know are
#     
#     assignment: =
#     addition/concatenation: +
#     subtraction: -
#     multiplication: *
#     floating point division: /
#     integer division: //
#     modulo: %
#     exponentiation: **
#     comparisons: <, <=, >, >=, !=, ==
#     Boolean Operations: or, and, not

# When we use + on two numbers, it works as addition just like in math, we can even use variables or even mix and match

# In[12]:


print(4 + 2)
print(a_int + a_float) # a_int = 6, a_float = 6.6
print(3 + a_int) # a_int = 6


# In[13]:


# Anything that comes after a # on the same line is a comment
# Python ignores it, but it lets us humans take notes on what we did


# When we use + on two strings, it concatenates them, we can use them with variables, strings, or both. + won't add spaces between strings though, so we have to do it manually.

# In[14]:


print(a_string + b_string)
print(a_string + " " + b_string)


# We can't mix and match strings and numbers though, if we want to, we have to "cast" them with Pythons quilt in casting system.

# In[15]:


value = 4
print(value)
print(type(value))
value = float(value)
print(value)
print(type(value))
value = str(value)
print(value)
print(type(value))


# now that value is a string, I can concatenate it with other strings

# In[16]:


print(a_string + " " + value + " " + b_string)


# assignment: =
# addition/concatenation: +
# subtraction: -
# multiplication: *
# floating point division: /
# integer division: //
# modulo: %
# exponentiation: **
# comparisons: <, <=, >, >=, !=, ==
# Boolean Operations: or, and, not
#     
# subtraction works the same way as addition, but only works with numerical vaules
# 

# In[17]:


print(a_float) # a_float = 6.6
print(a_float - a_int) # a_int = 6
# remember when I warned things would get weird?
# why this happens is a bit technical
# but its such a small amount you can effectivly ignore it


# In[18]:


print(5 * 3)
print(a_string * 3) # a_string = "hello"
# what would you do to get the string "hello hello hello"

print(2**4)


# In[19]:


print(5 / 3)
print(5 // 3) # this will drop the decimal part and floor it
print(5 % 2) # this gives us the remainder


# In[20]:


# comparison operators evaluate to bools
# its worth taking extra care: == is equals. = is assignment.
print(5 < 3)
print(5 > 3)
print(5 >= 5) # greater than or equal to
print(5 <= 4) # less than or equal to
print(5 != 4) # not equals
print(5 == 5) # equality!
print ("g" is "g") # is can be used to test equality of OBJECTS, will return different values than == for some things
# here is a reference with examples https://www.geeksforgeeks.org/difference-operator-python/


# In[21]:


# boolean values can be combined using or, and, & not
# evalutates to true if either one is true
print(True or False)
print(False or False)
# evaluates to true only if both are True
print(True and False)
print(False and False)
print(True and True)
# evaluates to the opposite value
print(not True)
print(not False)


# ### Collections

# A lot of the time, we will be working with a lot of numbers, and we need some way to arrange those numbers that makes sense. Python has a good range of collections to help us with this, the four most useful being:
# 
#     - Sets
#     - Lists
#     - Tuples
#     - Dictionaries

# ###### Sets
# 
# Sets are just like sets in math, they are a grouping of information that is NON ORDERED and DO NOT CONTAIN DUPLICATES

# In[22]:


# There is only one way to make an empty set
a_set = set()
# We can make one with information already in it if we want
a_set = {"dog", "fish", 42}

# to add to a set we use the Set.add() function
a_set.add("3")
a_set.add("dog")
# how would we add the number 3 to the set?
print(a_set)
# time for a new operator! in
# we can check to see if something is in our set using this

print("dog" in a_set)

#we can remove from the set with Set.remove()
a_set.remove("dog")

print("dog" in a_set)
print(a_set)


# ###### Lists
# 
# Now we'll talk about lists
# Lists are great when we have some ordered data we want to save

# In[23]:


# There are two ways to make an empty list (I recommend the first)
a_list = list()
a_list = []
# We can make one with information already in it if we want
a_list = [1,2,3,"dog","cat","fish","dog"]

# We can access a list just with []
print(a_list[2])
a_list[2] = "kitten"
print(a_list)

# We can add to the end of a list with List.append()
a_list.append("mouse")
a_list.insert(3, "hello") # add hello to the location of index 3

print(a_list)


# In[24]:


# There are a few ways to remove from a list
# List.pop() will remove and return the value at the LOCATION we want
# we can save it to a variable for later!
popped = a_list.pop(2)
# if we dont specify, the last element will be removed
a_list.pop()
print(a_list)
# if we know a value and want to remove THE FIRST TIME it occurs in our data
# we can use List.remove()
# since we already know what we want to get rid of, List.remove() doesnt return anything
a_list.remove("dog")

print(a_list)
print(popped)


# ###### Tuples
# 
# Next we'll touch on Tuples
# We use tuples when we have a small amount of ordered data we want to save

# In[25]:


# Theres only one way to make tuple
a_tup = (1,2,3,"dog")
# just like with a string, we can access a tuple using []
print(a_tup[1]) # remember we count from 0 in programming!


# Once we make a tuple, we can't change it. This is the reason we would pick a tuple over a List.
# If we want to change it, we have to make a new tuple
# we can however, assign that tuple to the same variable as the old one

# In[26]:


a_tup = (1,2,3,"dog") # so things don't break if you re-run
# a_tup[1] = 1 # python yells at us!
b_tup = (a_tup[0], "cat", a_tup[2], a_tup[3], "dog")
print(a_tup)
print(b_tup)
a_tup = (a_tup[0], "cat", a_tup[2], a_tup[3], "dog")
print(a_tup)


# ###### Dictionaries
# 
# Dictionaries have information stored in Key:Value pairs, it lets us associate data with other data rather than just an index (or location)

# In[27]:


# There are two ways to make an empty dictionary (I recommend the first)
a_dict = dict()
a_dict = {}
# if we want to make one with information already in it
a_dict = {"StudentNo":5555, "major":"Computer Science"}

# we can add to the dictionary by defining a new key
# if the key is already in the dictionary, we overwrite the old data, its gone forever
a_dict["zip"] = 30313
a_dict["StudentNo"] = 4444
print(a_dict)


# In[28]:


# If we know a key, we can go ahead and get the value from it
# If we want to save it for later we can store in in a variable
print(a_dict["major"])
# If we don't know a key, we can get a list of keys back!
print(a_dict.keys())
print(a_dict.values())

# if we want to remove something from the dictionary we use Dict.pop()
# we need to tell it what key we want removed
# it gives us the databack to save
popped = a_dict.pop("major")
print(a_dict)


# Tuples, Lists, Sets, and Dictionaries can hold any and all kinds of data we want. So we can put a List inside a List, a Dictionary inside a Dictionary, or a List inside a Set. Though its best to avoid doing this unless you need to.

# ### Aside: Code Blocks and Control Flow
# Python seperates code into (possibly nested) blocks through indentation / whitespace. These blocks get executed or skipped as a single unit.
# 
# Georgia Tech's CS Classes prefer (and I recommend) an intentation level of 4 spaces as the standard indentation level.
# 
# This is a complex topic; We'll explore and visualize code blocks and their execution as we discuss conditionals and loops in the following section.

# ### Conditionals

# Conditional statements are used to execute a certain command only if certain requirements are met
# the basic conditionals are if, elif, and else.
# 
# ifs are interpreted from start to end, so it will first interpret the if statement, then move to elif in the order they were written, then finally the else (note: elif and else ARE NOT required)

# In[29]:


print(a_tup)


# In[30]:


if "dog" in a_tup:
    print("bark")
elif "cat" in a_tup:
    print("meow")
else:
    print("I am not a dog or cat")


# We end the line containing the conditional with a :
# The : tells python that the next line should be a nested block of code; our print() statement in this case.
# 
# The elif conditional is only evaluated if the original if statement fails.
# the else conditional is only evaluated if both the original if statement and all elifs between fail.
# 
# Because the blocks of code associated with the elif conditional and the else conditional, we skip them as well.
# 
# 

# In[31]:


if "dog" in a_tup:
    # since there is an if directly after this, this if statement stands alone
    print("bark")
if "mouse" in a_tup:
    print("squeak")
else:
    # This else statement belongs to the If Directly above it.  The first if is independent
    print("I am not a dog or mouse")
# therefore both the first if, and the else statement are executed.


# ### For loops:
# Probably the most powerful tool in a programming language is the ability to interate over every item with one statement this is done using for loops Python has a very simple method for writing for loops

# In[32]:


# x is representing an item in the list
for x in a_list:
     print(x)


# In[41]:


#Two functions useful for going through a list are len() and range() len() will return an integer that is the length of a collection

#range() will generate a list of numbers we can use, usually in a loop we can call range with 1, 2, or 3 arguments

#if we pass one input to range(x), it generates a list from 0 to x
#if we pass two inputs to range(x,y) it generates a list from x to y
#if we pass three inputs to range(x,y,z) it generates a list from x to y using a step size of z. z can be negative


# In[35]:


# Here is a more complex for loop, utilizing if statements also
# this for look will first look for the length of list 1 (5 items), then will make x each number
# in that range (so will be 0,1,2,3,4) this is how you create that "classic" java or c++ loop 
for x in range(len(a_list)):
    if x > 2:
        print("I must be pretty big I'm " + str(x))
    else:
        print("I am still small.  I am only " + str(x))


# ### While Loops:
# On the other hand while loops will allow you to keep running a block of code until a condition is met. While a for loop can do the same thing as a while loop, they have different strengths for different use cases. A while loop to do the same thing as the for loop above is more complex

# In[36]:


# this accomplishes teh same thing as the above for loop
# would generally use the for loop instead of while loop in this case
i = 0
while i < len(a_list):
    print(a_list[i])
    i += 1


# In the above example, theres not really a reason to use a while loop instead of a for loop. But a while loop's condition can be anything, so it can be really powerful.

# In[37]:


# in this instance, the condition to loop is whether the item at the index in the list is not a string
# as soon as the item at the current index is a string we exit loop
i = 0
while type(a_list[i]) is not str:
    print(a_list[i])
    i += 1


# because anything that evaluates to a boolean can be used as a condition, we can use True and have a while loop run forever.
# 
# We're not running a web server though so we dont want that.
# 
# If we need to get out early, we can use the word break, which will always get you out of the most recent loop.
# 

# In[38]:


i = 0
while True:
        print("Hello! " + str(i))
        if i >= 5:
            break
        i += 1


# ### Functions:
# 
# Now that we have learned the basics, we are ready for functions, We've already been using them. When we want to use a function we use the f_name() format. So print(), range(), len(), type() are all functions python already gives to us!
# 
# functions are sections of code that are CALLABLE
# 
# that means throughout our code we can "summon" that code we created once to run
# 
# a function WILL NOT run unless called
# 
# A Parameter is a variable we can pass into a function in order to change the function's behavior

# In[39]:


def my_func(x, y): # we use def to define a function, then all parameters are inside the parentesis
    # this function multiplies 2 numbers together and returns that number
    z = x * y
    if z > 0:
        print(z)
    return z # functions with a return statement put the information after the return statement into 
# the variable defined when we call our function. return statements are optional.


# In[40]:


# Now we will test our function
print(my_func(2, 3))
return_val = my_func(2, 4)
print(return_val)
# notice how these variables now contain what we specified by the return statement


# Today we have learned everything from the basic Python types, all the way up to crafting simple functions. This is as far as this lesson will go. If anyone has any questions, I would be happy to clarify now!