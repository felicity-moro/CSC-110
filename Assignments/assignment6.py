import doctest

def get_powers(num_list:list, power)->list:
    '''
    takes all numbers in the list and takes them to the given power.
    returns the new list.

    >>> get_powers([1,2,3],2)
    [1, 4, 9]

    >>> get_powers([1,2,3],1)
    [1, 2, 3]

    >>> get_powers([],6)
    []

    >>> get_powers([-1,-2,-3],2)
    [1, 4, 9]

    >>> get_powers([-1.5,-2.5,-3.5],2)
    [2.25, 6.25, 12.25]

    '''
    lst = []
    if (len(num_list) == 0):
        return lst
    
    for index in range (len(num_list)):
        lst.append(num_list[index]**power) 

    return lst

def concatenate(lst:list[str])->str:
    '''
    takes a list of strings and returns them as one
    string

    >>> concatenate(["hello","world"])
    'hello world'

    >>> concatenate(["a","b","c","d"])
    'a b c d'

    >>> concatenate([])
    ''

    '''
    the_string = ""

    if (len(lst) == 0):
        return the_string
    
    for index in range (len(lst)):
        the_string += lst[index]
        if (index != len(lst)-1):
            the_string += " "

    return the_string

def contains_multiple(lst:list[int],number:int)->bool:
    '''
    returns wether or not any number in the given list is a multiple of the given
    number.
    >>> contains_multiple([1,2,3,4,5],2)
    True
    >>> contains_multiple([1,2,3,4,5],9)
    False
    >>> contains_multiple([1,2,3,4,5],0)
    False
    >>> contains_multiple([1,2,3,4,0],0)
    True
    >>> contains_multiple([],6)
    False
    '''

    if (len(lst) == 0):
        return False
         
    for index in range (len(lst)):
        if (number != 0) and (lst[index]%number == 0) :
            return True
        if (lst[index] == 0):
            return True

    return False

def get_long_enough(str_list:list[str],threshold:int)->list[str]:
    '''
    checks through the given list of strings and returns the list of strings with
    strings longer than the given threshold.

    >>> get_long_enough(["hello","world"],2)
    ['hello', 'world']

    >>> get_long_enough(["hello","world"],9)
    []

    >>> get_long_enough([],2)
    []

    >>> get_long_enough(["e","hi"],2)
    ['hi']

    '''

    lst = []
    if (len(str_list) == 0):
        return lst
    
    for index in range (len(str_list)):
        if len(str_list[index]) >= threshold:
            lst.append(str_list[index])
        
    return lst

def all_multiples(lst:list[int], multiple:int)->bool:
    '''
    checks if all integers in given list is a multiple of the given
    integer.

    >>> all_multiples([1,2,3,4,5,6],1)
    True
    >>> all_multiples([1,2,3,4,5,6],4)
    False
    >>> all_multiples([0,0,0,0],1)
    True
    >>> all_multiples([0,0,0,0],0)
    True
    >>> all_multiples([5,10,15,20],5)
    True
    >>> all_multiples([],9)
    True

    '''

    if (len(lst) == 0):
        return True
    
    for index in range(len(lst)):
        if (lst[index] != 0 and multiple == 0):
            return False
        elif (multiple != 0) and (lst[index]%multiple != 0):
            return False
        
    return True

def getting_shorter(lst:list[str])->bool:
    '''
    determines if the strings in the given list
    are getting smaller.

    >>> getting_shorter(["hello","hi","."])
    True

    >>> getting_shorter(["hello","hi","eeeee"])
    False

    >>> getting_shorter([])
    True

    >>> getting_shorter(["hi","hi","."])
    False

    >>> getting_shorter(["he","hippo","."])
    False

    '''

    if len(lst) == 0:
        return True
    
    prev = len(lst[0]*2)
    
    for index in range (len(lst)):
        if len(lst[index]) >= prev:
            return False
        prev = len(lst[index])
        
    return True