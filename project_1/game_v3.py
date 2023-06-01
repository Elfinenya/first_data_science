import numpy as np

def game_core_v3(number: int = 1) -> int:
    """A function that guesses a number in less than 20 tries.
       First you enter the values of the minimum and maximum number, 
       then set any random number. 
       We redefine the maximum, minimum and random number 
       depending on whether the random number is larger or smaller than the chosen number.
       The function accepts the puzzled number and returns the number of tries.
    Args:
        number (int, optional): puzzled number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    min_number = 0
    max_number = 100
    predict_number = np.random.randint(1, 101)

    while True:
      count += 1

      if predict_number > number:
          max_number = predict_number - 1
          predict_number = (max_number + min_number) // 2


      elif predict_number < number:
          min_number = predict_number + 1
          predict_number = (max_number + min_number) // 2

      else:
          break  # exit the cycle and end the game
    

    return count


def score_game(game_core_v3) -> int:
    """A function that finds the average number of attempts.
       What is the average number of guesses our algorithm makes in 10,000 tries.

    Args:
        game_core_v3 ([type]): Guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(1)  # fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(10000))  # riddled with a list of numbers
    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
if __name__ == '__main__':
    # RUN
    score_game(game_core_v3)