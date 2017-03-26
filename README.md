Micheal_Brewer_Hw3

Homework Assignment 3 Python Authors: Micheal Brewer CS 3030 – Hugo Valle

THe putpose of this script is to import a file from a website, in this case a log file. The script when then sort through the file and identify the top 25 errors and return a list of the errors and how many times they occurred. 

Script usage

Micheal_Brewer_Hw3.py

	$ python3 Micheal_Brewer_Hw3.py
	or
	./Micheal_Brewer_Hw3.py

What each defenition does


The help() demonstrates how the script is used. 

The test_arg() checks to see that an argument (sys.argv[1]) was put into the command. If so it will pass the the file info back to worked with. If not it will call the help().

The get_wrds() takes the argument url and decodes the file into readable text. It then creates the list errors[] and runs through each line in the file with a for loop which searches for four different critirias to match. if there are any matches the error path is appended to errors[].
It will then count the errors and the most common ones and list them into a viewable list displaying the top 25 errors and how many times they occured. 
	
The main() creates the url variable after calling test_arg() and getting the returned cile. It then passes the file to get_words().
attempts is set to 0 and increments to 3.

