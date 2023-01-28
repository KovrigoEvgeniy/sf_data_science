"""Auto-guess a number game
The program will both randomize numbers and guess them
"""

import numpy as np

def game_core_v3(number:int=1) -> int:
    """Guess a randomized number

    Args:
        number (int, optional): the number to auto-guess. Defaults to 1.

    Returns:
        int: number of attempts
    """
    
    count = 0
    guess_upper = 100
    guess_lower = 1
    predict_number = (guess_upper+guess_lower)//2 # Initial predicted number
    
    while True:
        count += 1
        if predict_number == number:
            break # Exit the While if guessed correctly
        elif predict_number < number:
            guess_lower = predict_number
        elif predict_number > number:
            guess_upper = predict_number
        
        # Predict a new number using updated boundaries
        # Treat the 99 edge case caused by rounding the average down 
        if predict_number == 99: 
            predict_number = 100 
        else:
            predict_number = (guess_upper+guess_lower)//2 
            
    return(count)


def score_game(game_core_v3) -> int:
    """Out of 1000 attempts how many tries it takes to guess on average

    Args:
        game_core_v3 (_type_): The function used for prediction

    Returns:
        int: average number of attempts used to guess
    """
    
    count_ls = [] # List used for storing the number of attempts
    np.random.seed(1) #Fixed seed for reproducibility
    random_array = np.random.randint(1,101, size=(1000)) # Prepare the numbers to guess
    
    for number in random_array:
        count_ls.append(game_core_v3(number))
        
    score = int(np.mean(count_ls)) # Finding the average number of attempts
    
    print(f'It took the program {score} attempts on average to guess the number') 
    return(score)


if __name__ == '__main__':
    # Run
    score_game(game_core_v3)