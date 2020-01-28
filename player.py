import hangman_real
import time
import sys

def get_indexes(letter, the_word):
	indexes = []
	for i,l in enumerate(the_word):
		if l == letter:
			indexes.append(i)
	return indexes

def convert_to_dict():
	f = open("analysis.txt", "r")
	d = {}
	for x in f.readlines():
		y = x.rstrip().split(":")
		a = y[0]
		b = y[1]
		d[int(a)] = b.split(",")
	return d

def main():
	the_word = input("Enter a word: ").lower()
	guess_word = ["-" for x in range(0, len(the_word))]
	d = convert_to_dict()
	hb = hangman_real.HangManAI("words_alpha.txt", d)
	chances = 10
	tries = 0
	while chances > 0:
		print("".join(guess_word))
		if "-" not in "".join(guess_word):
			print("Word Guessed Successfully\nThe word is: {}\nMistakes made: {}\nNumber of tries: {}".format(
				"".join(guess_word), 
				10 - chances, 
				tries))
			break
		g = hb.guess(guess_word)
		print("My guess:", g)
		indexes = get_indexes(g, the_word)
		if indexes != []:
			for index in indexes:
				guess_word[int(index)] = g
		else:
			chances -= 1
		tries += 1
	else:
		print("Failed to guess the word.")
		word = input("What is the word? ").lower()
		f = open("words_alpha.txt", 'r')
		for w in f.read().split("\n"):
			if word == w:
				print("This word is in my dictionary")
				break
		else:
			print("This word isn't in my dictionary, I'm going to add it")
			hb.append_to_dictionary(word)
if __name__ == "__main__":
	main()