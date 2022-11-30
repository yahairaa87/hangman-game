import random

list =["animals","bananas","roof","cow","cat","bark","storm","security","launch","prize","switch","view","freind","killer","widow","husband","scream","wednesday","march","christmas","cookies","danger","joke","salute","row","turnover","weekend","quarter","noise","main","bees","valentine","zombie","yoyo","green","purple"]  
print("Hello player. Lets play a game of hangman. You will be given a random word that you'll have to guess. Start off with one letter then continue to guess letters. You have six mistakes you can make.")

random_word = random.choice(list)
print(random_word)


def guessing_words(random_word):
  # random_word()
  # for i in random_word(): 
  #   return(i)
  approved_letters = [""]
  disapproved_letters = [""]
  for i in random_word:
    guess = input("Pick a letter from a-z!")
    print(f"You picked the letter {guess}")
    if i == guess:
      approved_letters.append(guess)
      print(approved_letters)
    else:
        disapproved_letters.append(guess)
        print("Nope, wrong guess.")

guessing_words(random_word)
# pickingwords()