import string
import random

def main():
	print("This random string generator will use all letters, numbers and punctuation to generate a random string (default behaviour).")
	while True:
		try:
			stringLength = int(input("Please enter a valid number for the length of random string:\n"))
			break
		except ValueError as e:
			pass

	randString = generateRandomString(stringLength)
	print("\nGenerated random string:\n\n" + randString)

def generateRandomString(expectedLen):
	# print(string.ascii_letters, string.digits, string.punctuation)

	randomCharPoolStr = string.ascii_letters + string.digits + string.punctuation
	randomCharPoolList = list(randomCharPoolStr)
	output = ""

	# Pick A Seed Based On Current Time: Random Assurance 1
	random.seed()
	# print(random.getstate())

	# Constantly shuffle the list of characters to be picked from: Random Assurance 2
	for i in range(0, 10000):
		random.shuffle(randomCharPoolList)
		# print(randomCharPoolList)

	randomCharPoolStr = ''.join(randomCharPoolList)
	# print(randomCharPool)
	# print(len(randomCharPool) - 1)

	# Pick Another Seed Based on Current Time: Random Assurance 3
	random.seed()

	# Randomly Pick Out Characters With New Seed: Random Assurance 4
	for i in range(0, expectedLen):
		randomIndex = random.randint(0, len(randomCharPoolStr)-1)
		# print(randomIndex)
		output+=randomCharPoolStr[randomIndex]

	return output

if __name__ == '__main__':
	main()