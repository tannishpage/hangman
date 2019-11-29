restriction = {0:"a", 1:"r", 2:"a"}
def get_words(length):
	file = open("words_alpha.txt", 'r')
	words = []
	for x in file.read().split("\n"):
		if len(x) >= 3:
			for r in restriction.keys():
				if x[r] != restriction[r]:
					break
			else:
				words.append(x)
	file.close()
	return words

y = get_words(10)
print(y)