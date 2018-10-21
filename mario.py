from cs50 import get_int

# Collects valid user input for height of pyramid
while True:
    height = get_int('Height: ')
    if height >= 1 and height <= 8:
        break

# Prints out left aligned pyramid line by line
for i in range(height):
    for k in range(height - i - 1):
        print(' ', end='')
    for j in range(i + 1):
        print('#', end='')
    print('')

