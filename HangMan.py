import random
from collections import Counter


words ='''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
# print(words)

words =words.split(' ')
answer = random.choice(words)
# print(answer)


if __name__ == '__main__':
    print("Welcome to Hangman game")

    for i in answer:
        print("_", end=" ")
    print()


    playing = True

    letterGuessed = ''
    chances = len(answer) + 2
    correct = 0
    flag = 0 #increases as the no. of correct choices increases


    try: 
        while (chances !=0) and flag == 0:
            print()
            chances -=1

            try:
                guess = str(input("Enter your guess: "))
            
            except:
                print('Enter only a letter')
                continue

            if not guess.isalpha():
                print("Enter only a letter!")
                continue
            elif len(guess)>1:
                print("Enter only a Single letter")
                continue
            elif guess in letterGuessed:
                print("Already guessed")
                continue

            if guess in answer:
                k = answer.count(guess)

                for _ in range(k):
                    letterGuessed += guess

            
            for char in answer:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(answer)):
                    print(char, end ='')
                    correct += 1

                elif (Counter(letterGuessed) == Counter(answer)):
                    print("The word is:", end="")
                    print(answer)
                    flag = 1
                    print("Congratulations, You won")
                    break
                    break

                else:
                    print('_', end = "")

            if chances <=0 and (Counter(letterGuessed)!= Counter(answer)):
                print()
                print("You lost! Try again")
                print('thw answer was {}'.format(answer))

    except KeyboardInterrupt:
        print()
        print("Bye")
        exit()


                


