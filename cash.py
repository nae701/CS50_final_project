from cs50 import get_float

# Collect valid user input on change owed
while True:
    change = get_float('Change owed: ')
    if change >= 0:
        break

# Converts change into a cent amount
cents = round(change * 100)

# Find the number of times each coin goes into cents then adds it to counter
coins = cents // 25
cents = cents % 25

coins += cents // 10
cents = cents % 10

coins += cents // 5
cents = cents % 5

coins += cents

print(coins)