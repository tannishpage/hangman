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
	the_words = open("words_alpha.txt", "r").read().split("\n")
	failed = []
	average_failed_guesses = 0
	average_tries = 0
	total = 0
	sys.stdout.write("Analyzing...")
	sys.stdout.flush()
	for x in the_words:
		if len(x) != 3:
			continue
		total += 1
		guess_word = ["-" for x in range(0, len(x))]
		d = convert_to_dict()
		hb = hangman_real.HangManAI("words_alpha.txt", d)
		chances = 10
		tries = 0
		while chances > 0:
			#print("".join(guess_word))
			#time.sleep(0.1)
			if "-" not in "".join(guess_word):
				#print("Word Guessed Successfully\nThe word is: {}\nMistakes made: {}\nNumber of tries: {}".format(
				#	"".join(guess_word), 
				#	10 - chances, 
				#	tries))
				average_failed_guesses = average_failed_guesses + (10 - chances)
				average_tries = tries + average_tries
				break
			g = hb.guess(guess_word)
			#print("My guess:", g)
			indexes = get_indexes(g, x)
			if indexes != []:
				for index in indexes:
					guess_word[int(index)] = g
			else:
				chances -= 1 
			tries += 1
		else:
			#print("Failed to guess the word.")
			failed.append(x)
			"""word = input("What is the word? ").lower()
			f = open("words_alpha.txt", 'r')
			for w in f.read().split("\n"):
				if word == w:
					print("This word is in my dictionary")
					break
			else:
				print("This word isn't in my dictionary, I'm going to add it")
				hb.append_to_dictionary(word)"""

	average_tries = average_tries / total
	average_failed_guesses = average_failed_guesses / total
	sys.stdout.write("Done\n\n")
	sys.stdout.flush()
	print("-------------- TEST SUMMARY -----------------\nFail To Total Ratio: {}/{}\nFail To Success Ratio: {}/{}\nAverage Number of Tries: {}\nAverage Failed Guesses: {}".format(len(failed),total,len(failed),total - len(failed),average_tries,average_failed_guesses))
if __name__ == "__main__":
	main()