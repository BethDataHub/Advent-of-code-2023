from aocd import get_data
import re

df=get_data(day=1,year=2023).splitlines()

def part_one():
    numbers = []
    for row in df:
        number = re.findall(r'\d',row)
        numbers.append(number)

    final_numbers=[]
    for number in numbers:
        final_numbers.append(int(f"{number[0]}{number[-1]}"))

    return sum(final_numbers)



def part_two():
    
    replacements={
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }

    pattern = r"(?=("+"|".join(list(replacements.keys()))+"))"

    numbers=[]
    for row in df:
        matches = re.findall(pattern,row.lower())

        if len(matches)>0:
            row = row.replace(matches[0],str(replacements[matches[0]])+matches[0],1)
            row = row.replace(matches[-1],str(replacements[matches[-1]])+matches[-1])

        number = re.findall(r'\d',row)
        numbers.append(number)

    final_numbers=[]
    for number in numbers:
        final_numbers.append(int(f"{number[0]}{number[-1]}"))
    
    return sum(final_numbers)