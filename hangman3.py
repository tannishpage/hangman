#libraries
import os
import random

#function
def openfile():
	file = open('3kwordlist.txt', 'r') 
	words = file.readlines()
	file.close()
	return words

def retry():
	print("do you wanna play again?yes/no")
	tryagain = input()
	if tryagain == "yes":
		game()
	elif tryagain == "no":
		exit()
	else:
		retry()

def modes():#from mode to modes
	modetype = input()
	if modetype == "1":
		mode1()
	elif modetype == "2":
		mode2()
	elif modetype == "3":
		mode3()
	elif modetype == "4":
		mode4()
	else: 
		print("please select one of the following options\n1.AI vs Player\n2.Player vs AI\n3.Player vs Player\nAI vs AI")
		mode()	

def mode1():#from mode1 to mode1
	attempts = 10
	word = random.choice(openfile()).rstrip()
	guessword = ["*" for x in range(0, len(word))]
	while attempts>0:
		print("you have",attempts,"attempts left")
		print("".join(guessword))
		print("guess a letter")
		usr_input=input()
		if len(usr_input) != 1:
			print("one letter please")
			continue
		if usr_input in word:
			for index in range(len(word)):
				if word[index] == usr_input:
					guessword[index] = usr_input
			if "".join(guessword) == word:
				break
		else:
			attempts -= 1
			print("you have",attempts,"attempts left")
			print("".join(guessword))
			print("sorry",usr_input,"was not in the word")
			continue
	if attempts == 0:
		print("hahahhaha you lose")
		print("the word was",word)
		retry()
	else:
		print("congratulations! you have guessed the word")
		print("The word was",word)
		retry()
		
def mode2():#from mode3 to mode2
	print("Player one has to make a word for Player 2, Player 2 look away!\nMake a word:")
	attempts = 10
	word = input()
	os.system("clear")
	attempts = 10
	guessword = ["*" for x in range(0, len(word))]
	while attempts>0:
		print("you have",attempts,"attempts left")
		print("".join(guessword))
		print("guess a letter")
		usr_input=input()
		if len(usr_input) != 1:
			print("one letter please")
			continue
		if usr_input in word:
			for index in range(len(word)):
				if word[index] == usr_input:
					guessword[index] = usr_input
			if "".join(guessword) == word:
				break
		else:
			attempts -= 1
			print("you have",attempts,"attempts left")
			print("".join(guessword))
			print("sorry",usr_input,"was not in the word")
			continue
	if attempts == 0:
		print("hahahhaha you lose")
		print("the word was",word)
		retry()
	else:
		print("congratulations! you have guessed the word")
		print("The word was",word)
		retry()

def mode3():
	alpbets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	#vowels = []
	#consonants = []
	wordlen = input("Enter length of word: ").lower()
	guessword = ["*" for x in range(0, int(wordlen))]
	count = 10
	while count > 0:
		print('Word: ' + ''.join(guessword))
		if '*' not in ''.join(guessword):
			did_i_win = input("Is %s the word? (y/n): " % ''.join(guessword)).lower()
			if did_i_win == 'y':
				print("Guess harder next time. haha GG. :)")
				retry()
		randoms = random.choice(alpbets)
		yn = input('Is ' + randoms + ' in the word? (y/n): ').lower()
		if yn == 'y':
			index = input("At what position(if more than one use spaces to seperate): ")
			index = index.split()
			for x in index:
				guessword[int(x)-1] = randoms
		else:
			count = count - 1
			
		del alpbets[alpbets.index(randoms)]
	else:
		input("Well tell me what the word is: ")
		print(random.choice(losing_responses))
		retry()


def game():
	print ("----------HANGAMN----------\nwhich mode would you like to pick?\n1.AI vs Player\n2.Player vs Player\n3.Player vs AI\n4.AI vs AI")
	modes()
#logic
losing_responses = ['Oh darn. Well I will try harder next time.', 'Damm..., I suck at hangman']
game()
