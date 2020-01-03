import os
import random

class HangManAI():
	def __init__(self, dictionary_path, analysis_data):
		"""
		Initializing the hangman bot with the path to the word dictionary, and
		the analysis data of the current dictionary.

		Parameters:
			dictionary_path (str): the path to the word dictionary
			analysis_data (dictionary<int>, list<str>): a dictionary
				containing the most common letters for a specified length
		"""
		self._dictionary_path = dictionary_path
		self._analysis_data = analysis_data
		self._guessed_letters = []
		self._vowles = ['a', 'e', 'i', 'o', 'u']
		self._can_guess_vowles = True
		self._consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
						 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
		self._can_guess_consonents = True
		self._most_common = self._get_most_common()


	def append_to_dictionary(self, word):
		"""
		Adds the given word to the dictionary
		Parameters:
			word (str) : the word to add to the dictionary
		"""
		dict_file = open(self._dictionary_path, "a")
		dict_file.write("\n{}".format(word))
		dict_file.close()

	def _get_analysis(self, length):
		"""(dictionary<int, str>)  returns the dictionary for the given length"""
		try:
			return self._analysis_data[length]
		except KeyError:
			return self._get_most_common()

	def _analyse_word(self, guess_word):
		"""(dictionary<int, str>) returns the restrictions"""
		restrictions = {}
		for n, l in enumerate(guess_word):
			if l != "-":
				restrictions[n] = l
		return restrictions

	def _get_words(self, length):
		"""(list<str>) Returns a list of words of the given length"""
		dict_file = open(self._dictionary_path, "r")
		words = []
		if length == 0:
			return dict_file.read().split("\n")
		for word in dict_file.read().split("\n"):
			if len(word) == length:
				words.append(word)
		return words

	def _get_letter_freq(self, words):
		"""(dict<str, int>) Returns the frequency of each letter"""
		letter_frequency = {}
		for word in words:
			for letter in word:
				if letter in letter_frequency.keys():
					letter_frequency[letter] = letter_frequency[letter] + 1
				else:
					letter_frequency[letter] = 1
		return letter_frequency

	def _filter_words(self, words, restrictions):
		filtered = []
		if restrictions == {}:
			return words
		for word in words:
			for restriction in restrictions.keys():
				if word[restriction] != restrictions[restriction]:
					break
			else:
				filtered.append(word)
		return filtered

	def _get_most_common(self, restrictions={}, length=0):
		words = self._get_words(length)
		filtered_words = self._filter_words(words, restrictions)
		letter_freq = self._get_letter_freq(filtered_words)
		maxes = []
		while True:
			try:
				maximum = max(letter_freq.values())
			except ValueError:
				return maxes

			for letter in letter_freq.keys():
				if letter_freq[letter] == maximum:
					maxes.append(letter)
					break
			letter_freq.pop(maxes[len(maxes)-1])
		return maxes
		

	def guess(self, guess_word):
		"""
		How Bot guesses:
			If the first guess or guessing when there weren't any successful 
			guesses then: guess from the most common letters for the length of
			the word.

			If more then four guesses but still no successful guesses then:
			guess the rest of the vowels (Find out most common to least common
			vowel)

			If still no successful guesses then: guess most common remaining 
			consonents

			After first successful guess, get most common letters of words with
			that letter in that position, and guess the most common letter that
			isn't already guessed

			After a few guess, if there is only one word left after retrieving 
			the list, then guess the letters from that word

			After a few guesses, if there are more then one word, continue guessing,
			if there is still more words and only one letter left, continue guessing.

			if guesses fail at this point, then the word given is unknown, and
			should just guess based on the most common letters that haven't been
			guessed yet
		Parameters:
			- guess_word (list<str>): A list containing dashes and correct 
				guesses
		"""
		restrictions = self._analyse_word(guess_word)
		if restrictions == {}:
			if len(self._guessed_letters) <= 4:
				guess = self._get_analysis(len(guess_word))[len(
					self._guessed_letters)]
				self._guessed_letters.append(guess)
				return guess
			elif self._can_guess_vowles:
				for v in self._vowles:
					if v not in self._guessed_letters:
						return v
				else:
					self._can_guess_vowles = False
			else:
				for c in self._consonents:
					if c not in self._guessed_letters:
						return c
				else:
					self._can_guess_consonents = False
		else:
			most_common = self._get_most_common(restrictions, len(guess_word))
			print(most_common)
			if most_common == []:
				most_common = self._most_common
			while True:
				for l in most_common:
					if l not in self._guessed_letters:
						self._guessed_letters.append(l)
						return l
				else:
					if len(self._guessed_letters) == 26:
						break
					most_common = self._most_common

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
	length = int(input("What is word length? "))
	guess_word = ["-" for x in range(0, length)]
	d = convert_to_dict()
	hb = HangManAI("words_alpha.txt", d)
	chances = 10
	tries = 0
	while chances > 0:
		if "-" not in "".join(guess_word):
			print("Word Guessed Successfully\nThe word is: {}\nMistakes made: {}\nNumber of tries: {}".format("".join(guess_word), 10 - chances, tries))
			break
		print("".join(guess_word))
		g = hb.guess(guess_word)
		i = input("Is {} in the word?".format(g))
		if i == "y":
			indexs = input("Where? ").split(",")
			for index in indexs:
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