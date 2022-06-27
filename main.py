import random

user_out = False
ai_out = False

user_score = 0
ai_score = 0

print("You will bat first")

while not user_out:
    user_choice = int(input("Choose any number between 1 to 6:"))
    ai_choice = random.randrange(1, 7)
    if user_choice == ai_choice:
        print(f"Your total is {user_score}")
        print(f"You selected {user_choice} and AI selected {ai_choice}")
        print("Ai needs", user_score+1, "run")
        print("Now it's AIs batting\n")
        user_out = True
    else:
        user_score = user_score + user_choice
        print(f"You scored {user_choice} more runs")
        print(f"Now your total is {user_score}\n")


while not ai_out:
    user_choice = int(input("Choose any number between 1 to 6:"))
    ai_choice = random.randrange(1, 7)
    if user_choice == ai_choice:
        print(f"AIs total is {ai_score}")
        print(f"You selected {user_choice} and AI selected {ai_choice}")
        if user_score == ai_score:
            print("It is a tie")
        elif ai_score<user_score:
            print(f"You won by {user_score-ai_score} runs")

        ai_out = True
    else:
        ai_score = ai_score + ai_choice
        print(f"AIs scored {ai_choice} more runs")
        print(f"Now AIs total is {ai_score}\n")
        if user_score<ai_score:
            print("AI won")
            break
