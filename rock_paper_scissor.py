import random

print("----- Rock Paper Scissor Game -----")
print("1. Rock \n2. Paper \n3. Scissor")

choice = ["rock","paper","scissor"]
user_score = 0
comp_score = 0
count = 5

for i in range(count):
    print("Attempt : " + str(i+1) + " of " + str(count))
    user_choice = int(input("Enter Your Choice : "))
    if user_choice not in [1,2,3,]:
        print("Invalid Choice !!!")

    user_pick = choice[user_choice - 1]
    comp_pick = random.choice(choice)
    print("You chose: " + user_pick)
    print("Computer chose: " + comp_pick)

    if (user_pick == comp_pick):
        print("Result : TIE !!!")
    elif (user_pick == "rock" and comp_pick == "scissors") or \
         (user_pick == "paper" and comp_pick == "rock") or \
         (user_pick == "scissors" and comp_pick == "paper"):
        print("Result: You Win this round!")
        user_score += 1
    else:
        print("Result: Computer Wins this round!")
        comp_score += 1

print("\n----- Game Over -----")
print("Your Score: " + str(user_score))
print("Computer Score: " + str(comp_score))

if user_score > comp_score:
    print("Congratulations! You are the Winner!")
elif comp_score > user_score:
    print("Computer Wins the Game!")
else:
    print("It's a Draw!")