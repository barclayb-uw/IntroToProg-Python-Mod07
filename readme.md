```
Barclay Bicksler
11/30/2020
IT FDN 110 A Au 20: Foundations Of Programming: Python
Assignment 07
```
# Exceptions and a Pickle, Sounds Fun

This week, the assignment took on an entirely different look as we were tasked with both finding more information about Python exceptions and the Python concept of Pickling as well as showing how they worked with our code examples.   I figured since the assignment was much different, I too would take a different tact in completing it.  Normally I will work on my code and once I have that usable I will jump over here and describe my journey, but this week I decided to start here and build the code as part of the story, hopefully it works out.  

So the first thing to decide is to start with Pickling or Exceptions, since I am a little more familiar with what an exception is I decided that I would start with Pickling.   To start, as anyone would expect I Googled Pickling in Python to get a list of search results I could use to gather data and examples.   I settled on two sites for the majority of my reading, [Geeks For Geeks](https://www.geeksforgeeks.org/understanding-python-pickling-example/) and [datacamp](https://www.datacamp.com/community/tutorials/pickle-python-tutorial)  I picked both because they provided a tutorial interspersed with code examples, which is they way I like to visualize new ideas.

So now to answer the big question, what is pickling.  Pickling in Python is a way to serialize and deserialize data from memory to disk.   The main reason you would want to do this is if you want to reconstruct the data in another Python script.   I also learned it was handly for transmitting the data over tcp/ip.   One thing to understand though is that Pickling is for Python only so it won’t work if you want to move data to another language.  That is an importing thing to remember.  

Here is a simple example of pickling, which includes screenshots from my code.  Figure 1 below will be pickling a dictionary, which is similar to the tutorial on the datacamp website.  
```
# example of using pickle to save a dictionary

# Step 1 - import Pickle into your python code
import pickle

# Step 2 - create my dictionary

my_dict = {'Frank': 47, 'Jane': 35, 'Butch': 27, "Linda": 51}

# now I have 3 peoples names and ages.

# Specify a filename to write to and then open the file for binary writing

filename = 'people'

outfile = open(filename,'wb')

# then use pickle.dump() to write to the file

pickle.dump(my_dict,outfile)
outfile.close()

# Now I will open the file to verify the data was saved correctly

infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()

# I will print the new dictionary to validate the data

print(new_dict)
# I can also compare it to my other dictionary
print(new_dict==my_dict)

```
###### Figure 1 : Saving a Dictionary with Pickle.

As you can see I created a simple dictionary file which gave me data to save, in this case some names and ages.  I then opened a file for writing in binary mode, which is very important as pickling requires binary writing.  With the file open I used the pickle.dump() function to save the data from the dictionary to the file.  Finally to validate the data was saved correctly I opened the file in a new dictionary, printed that data and also compared it to my original dictionary.   Yay! Everything worked.

Since you can pickle most data types this example can be extrapolated and used on more completed data, but the basic constructs remain the same. Now on to exceptions.

I once again went to Google for my initial foray into information on exceptions.  I found the site [Real Python](https://realpython.com/python-exceptions/) and once again [Geeks for Geeks](https://www.geeksforgeeks.org/python-exception-handling/) gave me the best combination of explanation and code.   
Exceptions occur when the Python code runs as it is intended to, but the code cannot process the result.   This is different from a syntax error like a missing parentheses because that will stop the code from running altogether, an exception may break the code, but only after it runs.  Exceptions will generally occur when you are bringing in data from an external source, like a file or asking a user to enter something.   Some common exceptions may be the file you are calling is not present or the case is incorrect, the user entered unexpected data like string characters instead of a number  or a resulting calculation tries to divide by zero.   When these exceptions occur they will throw an ugly although somewhat readable message on the screen.  This is ok, but not what the programmer intended so when creating code we need to make sure to try and capture any exceptions and handle them gracefully. 

Like I mentioned above there are several common exceptions.   In Python you can test for these exceptions by using a try statement in your code, this allows you to try the code and if an exception occurs you can tell the code to respond in a certain way.  This keeps the script running and may also let the user know what caused the issue.   To catch an exception you can use the combination of try and except .  Figure 2 is from the Real Python page that shows using try and except together.
```
try:
    linux_interaction()
except:
    pass
```
###### Figure 2 [https://realpython.com/python-exceptions/] simply try and except statement..  

This is great and will keep your code from throwing an ugly error, but since there are several different types of exceptions it is important to specify how you want your code to handle each one.  I decided to create a simple script that shows two common exception scenarios  and how to handle them.   In this code I will create a request for input of two numbers and divide those numbers for a result.   I will create exceptions if the users enter text instead of a number and another in case they try to divide by 0.    See Figure 3 below for my code.
```
# This script will ask for two numbers and return the product of them.
print('I will ask for two numbers and give you the product')
# Now I will start a try statement so I make sure numbers are entered
try:
    num1 = int(input('Please enter a number: '))
# If no number is entered exit with this message
except ValueError:
    print('I can only divide with numbers!')
else:
        # I need to do the same for the second number
    try:
        # If no number is entered exit with this message
        num2 = int(input('Please enter a second number: '))
    except ValueError:
        print('I can only divide with numbers!')
    else:
        # Now I need to make sure I am not dividing by 0
        try:
            num1 / num2
        except ZeroDivisionError:
            print('The second number cannot be Zero!')
        else:
            # If everything looks good, do the math!
            print(num1 / num2)
    
```
###### Figure 3: Code to validate data and divide by 0

There are a couple things to focus on in this example, first notice that instead of just using except: without any arguments, I am calling the specific exception.  How did I find these exceptions?  I ran my code and saw the output.  While the exception message is not something you want to show a user, it is very helpful to see when building the code.  I actually didn’t expect the ValueError: message when I started my sample, so that is a great example of using the code to help troubleshoot.  Once I had the exceptions I wanted to check for, it was a matter of making sure I was trying each one through the process.  In each of these steps my code will exit if an exception occurs, but it will tell the user why.  I could have made it more complex and looped it back after the error, but my main goal was to show how to capture the exceptions and this did that.  The try statement is very similar to an if statement and uses else to move to the next item. 

Hopefully these two sample help give you a better idea of what Pickling and Exceptions are in Python, they have by no means covered all there is to know, but they should provide an overview to get you started.   Both are important pieces to writing code and can be used in a variety of ways.   I enjoyed digging into these two concepts and look forward to seeing how we use these going forward.  





