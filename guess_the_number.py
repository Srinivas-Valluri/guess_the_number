from random import randint

number = randint(1,100)
guess = None
prev_guess = None
count=0
print(number)
while(True):
    count+=1
    guess = int(input('Enter a number: '))
    if number==guess:
        print(f'Yeah! correct guess after {count} tries and the number is {guess}')
        break
    if prev_guess==None and abs(number-guess)<11:
        print('WARM')
        prev_guess=guess
    elif prev_guess==None and abs(number-guess)>10:
        print('COLD')
    elif abs(number-guess)>10:
        print('COLD')
        prev_guess=None
    elif abs(prev_guess-number)>=abs(guess-number):
        print('WARMER')
        prev_guess = guess
    elif abs(prev_guess-number)<abs(guess-number):
        print('COLDER')
        prev_guess = guess
    
