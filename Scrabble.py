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
#user_word=input ("Word: ")
#print("Score: " + str(score_word(user_word)))

# Creating dictionary of words played by each player
player_to_words = {"player1":["blue", "tennis", "exit"], "wordNerd":["earth", "eyes", "machine"], "Lexi Con":["eraser", "belly", "husky"], "Prof Reader":["zap", "coma", "period"]}


# Dictionary to keep score
player_to_points={}

# Print list of words and their scores and calculate totalCalculate score
def keep_score():
	for player in player_to_words:
		print(player)
		player_points=0
		for word in player_to_words[player]:
			print(word + " : " + str(score_word(word)))
			player_points+=score_word(word)		
		player_to_points[player]=player_points
		print ("Total: "+str(player_points))
		print()

# Allow user to input new turns
def turn():
	for player in player_to_words:
		new_word = input(player + ": ")
		player_to_words[player].append(new_word)
	print()
	keep_score()

keep_score()
turn()