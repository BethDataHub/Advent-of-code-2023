from aocd import get_data
import numpy as np

df=get_data(day=2,year=2023).splitlines()

results={}
for game in df:
    game_number, game_data = game.split(":")
    results[game_number] = game_data


new_results={}
for key, value in results.items():
    rounds = value.split(";")
    new_results[key]=rounds

    rounds_dict={}
    for i, round in enumerate(rounds):
        round_elements=round.split(",")
        
        element_dict={}
        for element in round_elements:
            test=element.strip().split(" ")
            
            element_dict[test[1].strip()]=int(test[0].strip())
        rounds_dict[i] = element_dict
    new_results[key]=rounds_dict




def part_one():

    impossible_moves={
        "red":12,
        "green":13,
        "blue":14
    }

    impossible_games = []
    possible_games = []

    for game, rounds in new_results.items():
        for round, element in rounds.items():
            for color in ["red", "green", "blue"]:
                if element.get(color) and element.get(color) > impossible_moves[color]:
                    impossible_games.append(game)

    for game in new_results.keys():
        if game not in impossible_games:
            possible_games.append(int(game.replace("Game ", "").strip()))

    return sum(possible_games)


def part_two():
    game_highest_result={}
    for game, rounds in new_results.items():
        highest_result={}
        for round, element in rounds.items():
            for colour, quantity in element.items():
                if colour not in highest_result or quantity > highest_result[colour]:
                    highest_result[colour]=quantity
        game_highest_result[game]=np.prod(np.array(list(highest_result.values())))
    
    return sum(list(game_highest_result.values()))