def countdown(n): #function to count numbers from up to down and when a number equals to zero, there is a word "Blastoff!" on a screen.
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)


def countup(n): #function to count numbers when given a negative number and when a number equals to zero, there is a word "Blastoff!" on a screen.
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

user_number = int(input('Write a number here: '))
if user_number < 0:
    countup(user_number)
elif user_number > 0:
    countdown(user_number)
else:
    countdown(user_number)