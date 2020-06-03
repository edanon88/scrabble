# Codecademy scrabble project

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Creating points dictionary and adding blank tile
letters_to_points = {letter:value for letter,value in zip(letters,points)}
letters_to_points[" "]=0

# Function to calculate word score
def score_word(word):
	point_total=0
	for letter in word:
		point_total += letters_to_points[letter.upper()]
	return point_total

# Testing
user_word=input ("Word: ")
print("Score: " + str(score_word(user_word)))