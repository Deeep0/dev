secret_word = ["giraffe" , "parrot" , "lion"]

number = 1

while number <= 3 :
    guess = input("enter your guess. ")
    print(guess)
    number += 1
    if guess in secret_word:
        print("you won. ")
        break
    else :
        if number > 3:
            print("you lose. ")
        
