import random

fighters = ['rock', 'paper', 'scissor']

# The play game function will run the whole game with the fighters input as a list of strings.
def play_game(fighters):
    input("Welcome to your game! Press Enter to start.")
    print()

    # Starts the counters at zero.
    user_wins = 0
    computer_wins = 0

    while True:
        random_index = random.randint(0, 2)
        comp_choice = fighters[random_index]

        # Fill in the three with your chosen fighters. We use .lower() to make all the letters lowercase to avoid errors
        # for the user if they input choices with/without a capital letter.
        user_choice = input("rock, paper, or scissor").lower()
        while user_choice not in fighters:
            user_choice = input("That is not a valid choice. Please try again: ").lower()

        print()
        print("Your choice:", user_choice)
        print("Computer's choice:", comp_choice)
        print()

        # All the scenarios where user choice is [first fighter].
        if user_choice == 'rock':
            if comp_choice == 'rock':
                print("It's a tie!")
            elif comp_choice == 'paper':
                print("You win!")
                user_wins += 1
            elif comp_choice == 'scissor':
                print("You lose!")
                computer_wins += 1
        # All the scenarios where user choice is [second fighter].
        elif user_choice == 'paper':
            if comp_choice == 'paper':
                print("It's a tie!")
            elif comp_choice == 'rock':
                print("You win!")
                user_wins += 1
            elif comp_choice == 'scissor':
                print("You lose!")
                computer_wins += 1
        # All the scenarios where user choice is [third fighter].
        elif user_choice == 'scissor':
            if comp_choice == 'scissor':
                print("It's a tie!")
            elif comp_choice == 'paper':
                print("You win!")
                user_wins += 1
            elif comp_choice == 'rock':
                print("You lose!")
                computer_wins += 1

        print()
        print("You have " + str(user_wins) + " wins")
        print("The computer has " + str(computer_wins) + " wins")
        print()

        again = input("Play again? (Y/N) ").lower()
        while again not in ['y', 'n']:
            again = input("That is not a valid choice. Please try again: ").lower()

        if again == 'n':
            break

        print("\n----------------------------\n")

play_game(fighters)