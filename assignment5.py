import doctest
import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5

def roll_one_die()->int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    # this line MUST be uncommented when submitting to PrairieLearn
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # this line MUST be commented out when submitting to PrairieLearn
    #die = int(input('enter a simulated dice roll\n'))

    return die

def get_sequence(a:int, b:int, c:int)->str:
    '''
    Given three values, returns the sequence in form a + 1b, a + 2b until 
    the value reaches point c
    parameters : b cannot be 0.

    >>> get_sequence(2,5,32)
    '2,7,12,17,22,27,32'
    >>> get_sequence(2, 5, 31)
    '2,7,12,17,22,27'
    >>> get_sequence(1,1,5)
    '1,2,3,4,5'
    >>> get_sequence(0,2,8)
    '0,2,4,6,8'
    >>> get_sequence(8,4,8)
    '8'
    '''
    sequence = str(a)
    value = 0
    increment = 1
    while (value <= c and (a + increment*b) <= c):
        if (value < c):
            sequence += ","
        value = a + increment*b
        sequence += str(value)
        increment += 1
        
    return sequence

def digit_sum(n:int)->int:
    '''
    when given an int will return the sum of the digits
    int the number (absolute value only)

    >>> digit_sum(23)
    5
    >>> digit_sum(0)
    0
    >>> digit_sum(2)
    2
    >>> digit_sum(2789)
    26
    >>> digit_sum(200)
    2
    >>> digit_sum(-38)
    11
    '''
    n = abs(n)

    if n == 0:
        return 0
    
    if (n < 10):
        return n
    
    total = 0
    while (n!= 0):
        total += n%10
        n = n//10
    
    return total

def sum_factors(n:int)->int:
    '''
    sums all of the factors of the number given not including the
    number.

    precondition: number given is more than zero

    >>> sum_factors(5)
    1
    >>> sum_factors(12)
    16
    >>> sum_factors(8)
    7
    
    '''
    total = 0
    for count in range(1,n):
        if n%count == 0:
            total += count
    return total

def is_perfect(n:int)->bool:
    '''
    returns wether the given number is a perfect number:
    precondition: number is greater than zero

    >>> is_perfect(6)
    True
    >>> is_perfect(9)
    False
    >>> is_perfect(28)
    True
    >>> is_perfect(496)
    True
    >>> is_perfect(40)
    False
    >>> is_perfect(7)
    False
    '''
    if sum_factors(n) == n:
        return True
    else:
        return False
    
def n_perfect_numbers(n:int)->str:
    '''
    prints a list of perfect numbers the size of a the given number
    precondition: given number cannot be negative

    >>> n_perfect_numbers(0)
    ''
    >>> n_perfect_numbers(1)
    '6'
    
    >>> n_perfect_numbers(3)
    '6,28,496'

    >>> n_perfect_numbers(4)
    '6,28,496,8128'

    '''
    numbers = ''
    number = 6
    count = 0
    while (count != n):
        if is_perfect(number):
            numbers += str(number)
            count += 1
            if count != n:
                numbers += ','
        number += 1
    return numbers
        
#PART TWO CODE

def print_score(points:int,given_points:int)-> None:
    print (f"scored: {given_points} points")
    print(f"Total points: {points}")
    
def take_turn(player:str,points:int,round:int):
    '''
    takes a turn in the given round of Bunko when given the player name and points. returns
    the total points the given player has after the round.

    precondition: points > 0, 1 <= round <= 6
    ''' 
    initial_points = 999
    given_points = 0

    print(f"Player {player} is taking a turn in round {round}")

    while (points != initial_points and points < 21):

        initial_points = points
        given_points = 0

        roll_one = roll_one_die()
        roll_two = roll_one_die()
        roll_three = roll_one_die()

        print(f"Three dice rolled: {roll_one}, {roll_two}, {roll_three}")

        if (roll_one == roll_two and roll_one == roll_three and roll_one != round):
            given_points = 5
            points += given_points

        if (roll_one == round and (roll_two != round or roll_three != round)):
            given_points = 1
            points += given_points

        if (roll_two == round and (roll_one != round or roll_three != round)):
            given_points = 1
            points += given_points

        if (roll_three == round and (roll_two != round or roll_one != round)):
            given_points = 1
            points += given_points
                
        if (roll_one == round and roll_two == round and roll_three == round):
            points += 21
        
        print_score(points,given_points)
        print("\n")
    
    return points

def play_round(player1:str,player2:str,round:int)->str:
    '''
    plays a two player round of bunko. Asks for player names and the round they are playing.
    function prints winners name, points of both players, then returns the winners name.

    precondition: points > 0, 1 <= round <= 6

    '''

    p1_points = 0
    p2_points = 0
    winner = ''

    while (p1_points < 21 and p2_points < 21):

        if p1_points < 21 and p2_points < 21:
            p1_points = take_turn(player1,p1_points,round)

        if p1_points < 21 and p2_points < 21:
            p2_points = take_turn(player2,p2_points,round)
    if p1_points >= 21:
        winner = player1

    if p2_points >= 21:
        winner = player2
        
    print(f"Winner of this round is: {winner}")
    print(f"{player1} has {p1_points} points and {player2} has {p2_points} points")
    return winner

    

        

        

