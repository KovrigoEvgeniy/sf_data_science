"""Guess a number game"""

import numpy as np

number = np.random.randint(1,101) # generate a random number

# number of tries
count = 0

while True:
    count+=1
    predict_number = int(input("Guess a number between 1 and 100: "))
    
    if predict_number > number:
        print('Try a lower number')
    elif predict_number < number:
        print('Try a higher number')
    else:
        print(f'Correct! The number is {number}, took you {count} attempts')
        break # end of the While True