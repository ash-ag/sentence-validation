# Python program to validate a given sentence for a set of rules
# For the purposes of this problem, a “valid” sentence is defined as:
# 1. String starts with a capital letter.
# 2. String has an even number of quotation marks.
# 3. String ends with one of the following sentence termination characters: ".", "?", "!"
# 4. String has no period characters other than the last character.
# 5. Numbers below 13 are spelled out (”one”, “two”, "three”, etc…).

# Function to check a given sentence for given rules
def is_sentence_valid(sentence):

	# Constant to define numbers below rule #5
	NUMBER_BELOW_RULE = 13

	# Calculate the length of the string.
	length = len(sentence)

	# Check if empty sentence, it's invalid per rule #1 & #3
	if length < 1:
		return False

	# Check for #1 rule
	# 1. String starts with a capital letter.
	if sentence[0] < 'A' or sentence[0] > 'Z':
		return False

	# Check for #3 rule
	# 3. String ends with one of the following sentence termination characters: ".", "?", "!"
	if sentence[length-1] not in ['.', '?','!']:
		return False

	# Keep the index to the next character in the string.
	index = 1

	# counter for double quotation marks
	doubleQuoteMarkCounter = 0

	# Loop to go over the string.
	while(index < length):
		if sentence[index] in ["\"", "“", "”"]:
			doubleQuoteMarkCounter += 1
			index += 1

		# Check for #4 rule
		# 4. String has no period characters other than the last character.
		elif sentence[index] == "." and index != length-1:
			return False

		# Check for #5 rule
		# 5. Numbers below 13 are spelled out (”one”, “two”, "three”, etc…).
		elif sentence[index].isnumeric():
			numberStr = sentence[index]
			index += 1
			while index < length and sentence[index].isnumeric():
				numberStr += sentence[index]
				index += 1
			numberToCheck = int(numberStr)
			if numberToCheck < NUMBER_BELOW_RULE:
				return False
		else:
			index += 1

	# Check for #2 rule
	# 2. String has an even number of quotation marks.
	if doubleQuoteMarkCounter%2 != 0:
		return False

	return True


def main():
	# Driver program
	sentence = input("Enter sentence: ")

	if is_sentence_valid(sentence):
		print ("-->" + sentence + "<-- is valid")
	else:
		print ("-->" + sentence + "<-- is invalid")

if __name__ == "__main__":
	main()