""" Guess the Number Game """

import numpy as np


number = np.random.randint(1, 101) # generate random number
count = 0

while True:
    predict_number = int(input('Enter the number from 1 to 100: '))
    count += 1
    
    if predict_number > number:
        print('Your number is bigger. Try again')
    elif predict_number < number:
        print('Your number is less. Try again')
    else:
        print(f'Congratilation! You guessed the number {number} in {count} attempt(s)')
        break