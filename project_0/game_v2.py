""" Guess the Number Game v2
    Computer VS computer
"""

import numpy as np


def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Guessing the number and counting attempts
    
    Args:
        number (int, optional): Predict number. 
        Defaults is random generated number 1-100.

    Returns:
        int: Count of attempt(s)
    """    
    count = 0
    lst_num = list(range(101)) # generating list 0-100
    
    while True:
        count += 1
        predict_number = int(np.mean(lst_num)) # select mean number, loop1=50
        half = round(len(lst_num)/2) # find index of the middle of list
        if predict_number == number: break
        elif predict_number < number:
            lst_num = lst_num[half:]    # cut off the list, loop1=[50:100]
        lst_num = lst_num[:half]        # cut off the list, loop1=[0:49]
    return count


print(random_predict())