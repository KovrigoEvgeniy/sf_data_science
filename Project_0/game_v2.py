"""Auto-guess a number game"""

import numpy as np

def random_predict(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): the number to auto-guess. Defaults to 1.

    Returns:
        int: number of attempts
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101) # Predicted number
        if number == predict_number:
            break # Exit the While if guessed correctly
    return(count)

def score_game(random_predict) -> int:
    """Out of 1000 attempts how many tries it takes to guess on average

    Args:
        random_predict (_type_): The function used for prediction

    Returns:
        int: average number of attempts used to guess
    """
    
    count_ls = [] # List used for storing the number of attempts
    np.random.seed(1) #Fixed seed for reproducibility
    random_array = np.random.randint(1,101, size=(1000)) # prepare the numbers to guess
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # Finding the average number of attempts
    
    print(f'Your algo takes {score} attempts on average to guess the number') 
    return(score)


if __name__ == '__main__':
    # Run
    score_game(random_predict)