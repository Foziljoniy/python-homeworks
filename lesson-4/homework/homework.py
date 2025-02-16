from collections import Counter


#Problem 1

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)

    result = []

    # Elements in list1 but not in list2
    for num in count1:
        if num not in count2:
            result.extend([num] * count1[num])

    # Elements in list2 but not in list1
    for num in count2:
        if num not in count1:
            result.extend([num] * count2[num])

    return result

# Test cases
print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # Output: [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # Output: [2, 2, 5]

#Problem 2

def print_squares(n):
    for i in range(1, n):
        print(i ** 2)

# Example usage
n = 5
print_squares(n)


#Problem 3

def modify_string(txt):
    result = []
    vowels = "aeiouAEIOU"
    length = len(txt)
    
    i = 0
    while i < length:
        result.append(txt[i])

        # Check if it's the third character and not the last one
        if (i + 1) % 3 == 0 and i != length - 1:
            if txt[i] in vowels or (i + 1 < length and txt[i + 1] == '_'):
                result.append(txt[i + 1])
                i += 1  # Skip the next character
            result.append('_')
        
        i += 1

    return ''.join(result)

# Test cases
print(modify_string("hello"))  # Output: hel_lo
print(modify_string("assalom"))  # Output: ass_alom
print(modify_string("abcabcdabcdeabcdefabcdefg"))  # Output: abc_abcd_abcdeab_cdef_abcdefg


#probelem 4 
import random

def number_guessing_game():
    while True:
        secret_number = random.randint(1, 100)
        attempts = 10

        print("🎯 Welcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100. Try to guess it!")

        for _ in range(attempts):
            try:
                guess = int(input(f"Enter your guess ({attempts} attempts left): "))

                if guess < 1 or guess > 100:
                    print("⚠️ Please enter a number between 1 and 100.")
                    continue
                
                if guess < secret_number:
                    print("📉 Too low!")
                elif guess > secret_number:
                    print("📈 Too high!")
                else:
                    print("🎉 You guessed it right! 🎯")
                    return  # Exit game if guessed correctly
                
                attempts -= 1
                if attempts == 0:
                    print("❌ You lost. Want to play again? (Y/YES/y/yes/ok)")
                    break
            except ValueError:
                print("⚠️ Please enter a valid integer.")

        # Ask if the player wants to play again
        play_again = input().strip().lower()
        if play_again not in ['y', 'yes', 'ok']:
            print("👋 Thanks for playing! Goodbye!")
            break

# Start the game
number_guessing_game()


def check_password():
    password = input("🔑 Enter your password: ")

    if len(password) < 8:
        print("❌ Password is too short.")
    elif not any(char.isupper() for char in password):
        print("❌ Password must contain an uppercase letter.")
    else:
        print("✅ Password is strong.")

# Run the password checker
check_password()


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Print prime numbers between 1 and 100
print("Prime numbers between 1 and 100:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")


import random

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("Rock, Paper, Scissors Game! First to 5 points wins.")

while player_score < 5 and computer_score < 5:
    player_choice = input("\nChoose rock, paper, or scissors: ").lower()
    if player_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = get_winner(player_choice, computer_choice)
    
    if result == "player":
        player_score += 1
        print("You win this round!")
    elif result == "computer":
        computer_score += 1
        print("Computer wins this round!")
    else:
        print("It's a draw!")

    print(f"Score -> You: {player_score}, Computer: {computer_score}")

# Final winner
if player_score == 5:
    print("\n🎉 Congratulations! You won the match!")
else:
    print("\n💻 Computer wins the match. Better luck next time!")

