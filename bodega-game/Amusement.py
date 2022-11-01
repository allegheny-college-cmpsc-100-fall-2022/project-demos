import json
import random

FILE_LIST = {
	"data/words/nouns.json": "nouns",
	"data/words/adjs.json": "adjs",
	"data/words/adverbs.json": "adverbs"
}

def load_words() -> list:
	final_words = []
	for file in FILE_LIST:
		fh = open(file)
		words = json.load(fh)
		for word in words[FILE_LIST[file]]:
			if len(word) == 5: 
				final_words.append(word.lower()) 
	return final_words

def mask_letters(letters: list = []) -> str:
	for letter in letters: 
		idx = letters.index(letter)
		letters[idx] = "_"
	return letters

def get_letters(word: str = "") -> list:
	letters = []
	for letter in word:
		letters.append(letter)
	return letters

def restore_letter(word: str = "", guess: str = "", masked: list = []) -> list:
	correct = get_letters(word)
	if guess in correct:
		idx = correct.index(guess)
		masked[idx] = guess
	return masked

def check_win(guess: list = []) -> bool:
	if "_" in guess:
		return False
	return True

def main():
	words = load_words() 
	word = random.choice(words)
	letters = get_letters(word)
	masked = mask_letters(letters) 
	print(f"Your word: {' '.join(masked)}")
	while True:
		guess = input("Guess a letter: ")
		result = restore_letter(word, guess, masked)
		print(f"Your word: {' '.join(result)}")
		win = check_win(result)
		if win:
			print(f"You won! Your word was {word}!")
			break
		if guess == "quit":
			print(f"You gave up! Your word was {word}!")
			break

# Do not alter ------------------
if __name__ == "__main__":
	main()
# Do not alter ------------------