import os
def get_words(length):
	file = open("words_alpha.txt", 'r')
	restriction = {3:"a", 2:"n", 0:"b", 5:"i"}
	words = []
	for x in file.read().split("\n"):
		if len(x) == length:
			for r in restriction.keys():
				if x[r] != restriction[r]:
					break
			else:
				words.append(x)
	file.close()
	print(words)
	return words

def make_dict(words):
	l = {}
	for x in words:
		for y in x:
			if y in l.keys():
				l[y] = l[y] + 1
			else:
				l[y] = 1
	return l

def get_three_max(thingo):
	maxes = []
	while True:
		#print(thingo)
		maximum = max(thingo.values())
		if len(maxes) == 6:
			break
		for y in thingo.keys():
			if thingo[y] == maximum:
				maxes.append(y)
				break
		thingo.pop(maxes[len(maxes)-1])
			
	return maxes

file = open("analysis.txt", "w")
for x in range(6, 20):
	words = get_words(x)
	if words == []:
		break
	l = make_dict(words)
	#file.write("{}:{}\n".format(x, ",".join(get_three_max(l))))
	print(x, ":", ",".join(get_three_max(l)), sep="")
	print(words)