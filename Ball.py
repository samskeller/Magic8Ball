'''
Written by Sam Keller

This is the Ball class needed to make a magic 8-ball

The class has a number of methods, each of which corresponds to the options possible
in the M8ball.py main file
'''

import random

class Ball: 

	""" The M8ball class is the meat of the program-- in it, we define some methods
	that give us the ability to change the bias of the 8-ball, shake the 8-ball, view
	the current bias value, and quit the program """
	
	def __init__(self, bias):
		self.bias = bias
		
	def positive(self):
	
		""" The positive method lowers the bias value by 1, making the answers more
		likely to be positive responses"""
	
		self.bias = self.bias - 1
		if self.bias < 0:
			self.bias = self.bias + 1
			print "Sorry, you can't have a bias value of less than zero."
		else:
			print "Your current bias number is: ", self.bias
	
	def negative(self):
	
		""" The negative method lowers the bias value by 1, making the answers more
		likely to be negative responses"""
	
		self.bias = self.bias + 1
		if self.bias > 4:
			self.bias = self.bias - 1
			print "Sorry, you can't have a bias value of more than four."
		else:
			print "Your current bias number is: ", self.bias
	
	def getBias(self):
	
		""" The getBias method prints the current bias value"""
	
		print "Your current bias value is: ", self.bias
	
	def shake(self):
	
		""" The shake method produces a Magic 8-ball response. It uses the current 
		bias value to determine the probabilities ofgetting each of the responses. 
		Then, it makes a list with ten components, each of which is one of the 
		possible responses. The higher the probability of a response, the more times
		it appears in the list. That way, when there's a random selection from the 
		list, more probable answers will be chosen on a more regular basis."""
	
# Here we make the probabilities, based on the bias number

		proba = .2 + (2 - self.bias)/10.0
		probb = .2 + (2 - self.bias)/10.0
		probc = .2
		probd = .2 + (self.bias - 2)/10.0
		probe = .2 + (self.bias - 2)/10.0
		
# Then we create a list and fill it with the correct number of each response, 
# depending upon their probability values

		list = []
		n = 1
		while n <= (proba * 10):
			list.append('Definitely')
			n = n + 1
		n = 1
		while n <= (probb * 10):
			list.append('Perhaps')
			n = n + 1		
		n = 1
		while n <= (probc * 10):
			list.append('Not sure')
			n = n + 1
		n = 1
		while n <= (probd * 10):
			list.append('Unlikely')
			n = n + 1
		n = 1
		while n <= (probe * 10):
			list.append('No Way')
			n = n + 1	

# Now we take a random sample from this list of ten responses

		answer = random.sample(list,1)
		print 'The answer to your question is: ', answer[0]