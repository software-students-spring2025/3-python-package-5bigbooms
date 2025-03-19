import random

#predefined list 
brainrot_list = {
     "Haliey Welch": ["hawk tuah, spit on that thang"],
     "The Costco Guys": ["We're so sorry to hear about your brother that passed away he gets five big booms", ""]
}

# Hall of fame function
# arguments: integer number
# return: random names from list
def hall_of_fame(n: int):
    if n <= 0:
        return []
    # ensure no error messages
    return random.sample(brainrot_list, min(n, len(brainrot_list)))


# Random capitalization function
# arguments: string phrase
# return: string with mixed capitalization
def random_capitalization(phrase: str):
    result = ""
    for i in range(len(phrase)):
            result += phrase[i].upper if i % 2 == 1 else phrase[i]
    return result 
        


