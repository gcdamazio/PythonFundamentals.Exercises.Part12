from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start: This is where the list of numbers starts.
    :param stop: 
    :param parity:
    :return:
    """
    if parity == Parity.ODD:
        return [x for x in range(start,stop) if x % 2 != 0]
    elif parity == Parity.EVEN:
        return[x for x in range(start,stop) if x % 2 ==0]
    else:
        return []    
    
    # Explanation:
    #start: where the list of numbers starts
    #stop: where the list of number ends, but the stop number is not included
    #parity: tells the func.if i want odd numbers or even numbers
    #Parity.ODD - Goes to the list and pick the ODD ones / Paritt.EVEN - goes to the list and pick the EVEN ones


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    return {x: strategy(x) for x in range(start, stop)}
    # start: This is the first number you want to start with.
    # stop: This is the last number, but the function doesn’t include this one. It stops right before it.
    #strategy: this function give me to decide what the value each  number should be. Ex. maybe I want a number doubled or the number squared




def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    return set(char.upper() for char in val_in if char.isalpha())