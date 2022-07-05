""" Guess the Number Game v2
    Computer VS computer
"""

import numpy as np


def random_predict(number: int=1) -> int:
    """Guessing the number by generating random number
    
    Args:
        number (int, optional): Predict number from score_game(). 
        Defaults to 1.

    Returns:
        int: Count of attempt(s)
    """    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # computer trying to guess
        if number == predict_number:
            break
    
    return count


def score_game(random_predict) -> int:
    """Mean of Guess the Number

    Args:
        random_predict (_type_): Predict function

    Returns:
        int: The mean of algorithm
    """
    count_ls = [] # list of counts of attempts
    np.random.seed(1) # fix the seed for generating the same random
    # generate numbers to array for random_predict()
    random_array = np.random.randint(1, 101, size=(1000)) 
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # calculate mean via numpy bi-function
    print(f'The mean of the Guess the Number algorithm is: {score}')
    
    return score

# call function for module
if __name__ == '__main__':
    score_game(random_predict)
    
# test