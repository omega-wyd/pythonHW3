Micheal_Brewer_Hw3

Homework Assignment 3 Python Authors: Micheal Brewer CS 3030 – Hugo Valle

The purpose of this script Micheal_Brewer_Hw3.py is to replicate how an ATM accepts a user input of their pin and verifies that it meets the requirments of 1) being only numbers, 2) is 4 characters long, 3) macthes the rtequired pin.

Script usage

Micheal_Brewer_Hw2.py

	$ python3 Micheal_Brewer_Hw2.py
	or
	./Micheal_Brewer_Hw2.py
What each defenition does

pin is set to userinput

The check() def takes the argument of pin. It will test right off if the pin equals the hardcoded pin of 1234.

The length() def takes the argument of pin. It checks to see if the pin is 4 characters long. If not it prints (" Invalid PIN lenth. Correct format is: <9876>").

The num() def takes the argument of pin. It checks to see if pin is all numeric characters. If not it prints (" Invalid PIN character. Correct format is: <9876>").

The getInput() def takes the argument pin. It runs a whie loop thatasks the user to input a pin and only allow 3 attempts to enter the correct pin. It calls defs check(), length(), and num() in the loop to check each of the user's inputs.

attempts is set to 0 and increments to 3.

The main() def calls the getInput() to start the process.
