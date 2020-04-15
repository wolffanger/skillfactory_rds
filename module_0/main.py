import numpy as np

def game_core_v2(number):
    
    count = 0
    predict = 50
    division_number = predict
    lower_threshold = predict - predict
    upper_threshold = predict * 2

    for i in range(0, 4):
       
        if division_number == number: 
            count += 1
            return(count)
            break

        if number > division_number:
            lower_threshold = division_number
            division_number = int(lower_threshold + ((upper_threshold - lower_threshold) // 2))
        
        elif number < division_number:
            upper_threshold = division_number
            division_number = int(lower_threshold + ((upper_threshold - lower_threshold) // 2))

    for i in range(lower_threshold, upper_threshold + 1):
        count+=1
        if i != number:
            continue
        else:
            return(count)
            break

def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v2)