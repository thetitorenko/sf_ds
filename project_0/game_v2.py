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

def score(random_predict) -> int:
    """Runs main function 1000 times

    Args:
        random_predict (_type_): Main function

    Returns:
        int: Minimun count of attempts after 1000 times
    """    
    counter_ls = []
    for i in range(1000): # run main function 1000 times
        counter_ls.append(random_predict())
    result = int(np.mean(counter_ls)) # calculate mean
    
    return result


print(f'The minimum count of attempts, during 1000 times, is {score(random_predict)}')