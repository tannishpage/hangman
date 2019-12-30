import os
import random

class HangManAI():
	"""
	"""

	def __init__(self, dictionary_path, analysis_data):
		"""
		Initializing the hangman bot with the path to the word dictionary, and
		the analysis data of the current dictionary.

		Parameters:
			dictionary_path (str): the path to the word dictionary
			analysis_data (dictionary<int, list<str>): a dictionary
				containing the analysis done on word length
		"""
		self._dictionary_path = dictionary_path
 		self._analysis_data = analysis_data
		self._guessed_letters = []
		self._guess_number = 0
		self._tick = 0
		self._vowles = ['a', 'e', 'i', 'o', 'u']
		self._consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
						 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


	def _append_to_dictionary(self, word):
		"""
		Adds the given word to the dictionary
		Parameters:
			word (str) : the word to add to the dictionary
		"""
		dict_file = open(self._dictionary_path, "ab")
		dict_file.write(bytes("{}\n".format(word).encode("utf-8")))
		dict_file.close()

	def _get_analysis(self, length):
		"""(dictionary<int, str>)  returns the dictionary for the given length"""
		return self._analysis_data[length]

	def _analyse_word(self, word):
		restrictions = {}
		for n, l in enumerate(guess_word):
			if l != "-":
				restrictions[n] = l
		return restrictions

	def _get_words(self, length):
		pass

	def _make_freq_dict(self, words):
		pass


	def _get_most_common(self, restrictions={}, length=0):
		

	def guess(guess_word):
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
			else:
				picked = False
				for v in self._vowels:
					if v not in self._guessed_letters:
						return v
		else:
			most_common = self._get_most_common(restrictions, len(guess_word))
			if most_common == []:
				most_common = self._get_most_common()
			for l in most_common:
				if l not in self._guessed_letters:
					return l
		




