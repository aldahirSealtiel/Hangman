import random
# Write your code here
chances = 8
letters_discovered = 0
letters_used = set()

print("H A N G M A N")

command = input('Type "play" to play the game, "exit" to quit:')
if command == 'play':
    answers = ['python', 'java', 'kotlin', 'javascript']
    random.seed()
    answer = answers[random.randint(0, len(answers) - 1)]
    discovered = []

    for _ in range(len(answer)):
        discovered.append(False)

    while chances > 0 and letters_discovered < len(answer):
        print()
        show_letters = ""
        for i in range(len(answer)):
            if not discovered[i]:
                show_letters += "-"
            else:
                show_letters += answer[i]
        print(show_letters)
        guess = input("Input a letter:")
        if len(guess) != 1:
            print("You should input a single letter")
            continue
        if not 'a' <= guess <= 'z':
            print("It is not an ASCII lowercase letter")
            continue

        if guess in letters_used:
            print("You already typed this letter")
            continue
        letters_used.add(guess)

        if guess in answer:
            is_discovered = True
            for j in range(len(answer)):
                if answer[j] == guess:
                    if not discovered[j]:
                        discovered[j] = True
                        letters_discovered += 1
                    else:
                        is_discovered = False
            if not is_discovered:
                print("No improvements")
                chances -= 1
        else:
            print("No such letter in the word")
            chances -= 1

    if chances > 0 and letters_discovered == len(answer):

        print("You guessed the word {answer}!".format(answer=answer))
        print("You survived!")
    else:
        print("You are hanged!")

#print("Thanks for playing!")
#print("We'll see how well you did in the next stage")
