# M8ball.py
# 
# Written by Sam Keller on March 29th, 2011
#
# This program gives the user access to an 8-ball on a computer! However, this 8-ball
# can be a little biased. There are five different possible responses from the computer,
# but the user can give the 8-ball a bias by giving it a bias value of a number
# between 0 and 4. Values of 0 and 1 are biased towards positive responses, 3 and 4 are biased
# towards negative responses, and 2 is a neutral bias. In addition to shaking the
# 8-ball and seeing what response comes out, the user can change the bias number
# from the command line. 

from Ball import *

def printMenu():

	""" The printMenu function is a simple function that prints the different possibilities
	for the user to choose from. The menu is reprinted after every time an action is taken"""

	print 'p: Lower the bias by 1'
	print 'n: Raise the bias by 1'
	print 's: Shake the Magic 8-ball for an answer to your question'
	print 'b: Print the current bias number'
	print 'q: Quit'
	print
	
def chooseOperation(selection, eightball):

	""" The chooseOperation function takes the response from the user for which option 
	they would like to choose and then does the appropriate method from our M8ball class."""
	
	if selection == 'p':
		print
		eightball.positive()
	elif selection == 'n':
		print
		eightball.negative()
	elif selection == 's':
		print
		eightball.shake()
	elif selection == 'b':
		print
		eightball.getBias()
	else:
		print
		print "Sorry, that's not one of the options."

def main():

	""" This is the main part of the program. It first asks for an initial bias value.
	If the initial value is not a number 0-4, it asks you to try again. If it is, 
	it sets an instance of the class M8ball and then runs a while loop which 
	loops the menu until the quit option is chosen."""
	
	n = 1
	while n == 1:
		bias = raw_input('What would you like your initial 8-ball bias value to be? (0-4) ')
		if bias == '0' or bias == '1' or bias == '2' or bias == '3' or bias == '4':
			eightball = Ball(int(bias))
			k = 1
			while k == 1:
				print
				printMenu()
				response = raw_input('Please choose one of these options: ')
				if response == 'q':
					print 'All done!'
					k = 2
					n = 2
				else:
					chooseOperation(response, eightball)
		else:
			print "Sorry, that's not a valid value for the initial bias. Please try again"

# Here is where we execute all of our functions and our class!

if __name__ == '__main__':
	main()
	
# The program is now finished!