import random

def main():

    num_dice = int(input("Enter the number of dice to roll: "))

    if num_dice <= 0:
        print("The number of dice must be a positive integer.")
        return

    total_sum = 0

    for _ in range(num_dice):
        roll = random.randint(1, 6)
        total_sum += roll

    print(f"The sum of the numbers rolled is: {total_sum}")

if __name__ == "__main__":
    main()
