from random import choice
guesses = 0
words = ["badger", "Joker", "batman", "superman",
         "luther", "flash", "savitar", "alice", "djokovic", "lakers", "lebron", "cavaliers", "laptop"]
guess = choice(words)
new = [x for x in guess]
print(len(new))
while guesses <= len(new):
    g = input("Choose a Letter: ").lower()
    if g in new:
        print("Good")
    if guesses == len(new):
        if g != guess:
            print(f" The right answer is {guess}")
    if g == guess:
        print("You got it!! :)")
        break
    else:
        guesses += 1
        print("Try Again")
