"""restriction = {0:"a", 1:"r", 2:"a"}
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
print(y)"""

def binsearch(searching, nums):
	min = 0
	max = len(nums)
	mid = int(max/2)
	while True:
		print(min, mid, max)
		mid = int(min + (max - min)/2)
		if searching > nums[mid]:
			min = mid
		elif searching < nums[mid]:
			max = mid
		else:
			return mid
print(binsearch("be", open("words_alpha.txt", 'r').read().split("\n")))