#Variable Declaration
secret_number=9
guess_count=0
guess_limit=3

print("Guess the Secret No between 1 - 10 (3 Attempts)")

while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count+=1
    if guess==secret_number:
        print("You Won !!!")
        break
