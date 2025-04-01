import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_toss(n):
    r = {"Heads": 0, "Tails": 0}
    
    for _ in range(n):
        output = coin_toss()
        r[output] += 1
    
    heads_percentage = (r["Heads"] / n) * 100
    tails_percentage = (r["Tails"] / n) * 100
    
    print(f"\nResults after {n} flips:")
    print(f"Heads: {r['Heads']} ({heads_percentage:.2f}%)")
    print(f"Tails: {r['Tails']} ({tails_percentage:.2f}%)")

while True:
    try:
        n = int(input("Enter the number of times to flip the coin: "))
        if n <= 0:
            print("Please enter a positive integer.")
            continue
        multiple_toss(n)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
        
    restart = input("Do you want to flip again? (yes/no): ").strip().lower()
    if restart != 'yes':
        print("Thanks for playing! Goodbye.")
        break
