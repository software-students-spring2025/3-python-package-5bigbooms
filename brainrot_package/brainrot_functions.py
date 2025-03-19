import random

#predefined list 
hall_of_fame_list = [
    #Tony's list
]

# Hall of fame function
# arguments: integer number
# return: random names from list
def hall_of_fame(n: int):
    if n <= 0:
        return []
    # ensure no error messages
    return random.sample(hall_of_fame_list, min(n, len(hall_of_fame_list)))


# Random capitalization function
# arguments: string phrase
# return: string with mixed capitalization
def random_capitalization(phrase: str):
    result = ""
    for i in range(len(phrase)):
            result += phrase[i].upper if i % 2 == 1 else phrase[i]
    return result 
        


