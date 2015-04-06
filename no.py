#NUM guessing game which was tough to make
import random
import time
 
guesses_taken = 0
name = raw_input('what is your name?')
print ('nice to meet you ' + name)
time.sleep(2)
print('lets play a guessing game. I have a number between 1 to 100. Can you try to guess it within 10 chances? ')
time.sleep(2)

NUM = random.randint(1,100)
#print ('Random number is '+ str(NUM))

while guesses_taken < 10:
	guess = int(raw_input(' number of guesses used '+ str(guesses_taken)+' guess my number: '))
	if guess == NUM:
		print("correct! you guessed my number in " + str(guesses_taken) + " guesses!")
		print("Exiting the programme Good Bye")
		break
	elif guess > NUM:
		print('Your guess number is larger than my number try again')
	else:
		print('Your guess number is smaller than my number try again')
	guesses_taken += 1              
if guess != NUM:
	print("oh! you couldnt guess it in 10 chances the NUM was " + str(NUM) + "  better luck next time")
	print("Exiting the programme Good Bye")

