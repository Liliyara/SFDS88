"""The computer creates a number and guesses it as efficiently as possible"""

import numpy as np


def random_predict(number:int=1) -> int:
    count = 1
    max = 100
    min = 1
    result = round((max + min) / 2)
    while result != number:
        if result > number:
            max = result
            result = round((max + min) / 2)
        else:
            min = result
            result = round((max + min) / 2)
            
        count += 1
        if count>1000:
            break

    return count


def score_game(random_predict) -> int:
    """How many tries does it take on average to guess
        
    Args:
        rundom_predict (_type_): guess function
            
    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(1) # fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))

    
        
    score = int(np.mean(count_ls))
    print('Your algorithm guesses the number on average in: {} attempts'.format(score))
    return(score)


if __name__ == '__main__':
    # run
    score_game(random_predict)