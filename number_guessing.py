from random import randint

def guessnumber(n_user, n_bot):
    if n_user == n_bot:
        return "You win! Your number: "+str(n_user)+" My number: "+str(n_bot)
    else:
        return "You loose! Your number: "+str(n_user)+" My number: "+str(n_bot)

answer = "y"
while answer == "y":
    user_number = int(input("Choose a number between 1 and 10: "))
    bot_number = randint(1, 10)
    print(guessnumber(user_number, bot_number))
    answer = (input("Want to play again? [y, n]"))
