import doctest

Flight = tuple[str,str,float]
DEPARTURE = 0
ARRIVAL = 1
DURATION = 2

def swap(lst:list, pos_a:int, pos_b:int)->None:
    '''
    swaps values in a list at the given positions.

    >>> list_vals = [1,2,3,4,5]
    >>> list_words = ["world","hello"]
    >>> empty = []


    >>> swap(list_vals,0,1)
    >>> list_vals
    [2, 1, 3, 4, 5]

    >>> swap(list_words,0,1)
    >>> list_words
    ['hello', 'world']

    >>> swap(empty,0,0)
    >>> empty
    []

    >>> swap(list_vals,4,4)
    >>> list_vals
    [2, 1, 3, 4, 5]

    '''
    if (len(lst) == 0):
        return
    
    holder = lst[pos_a]
    lst[pos_a] = lst[pos_b]
    lst[pos_b] = holder

def index_of_smallest(lst:list)->int:
    '''
    returns the index of the smallest value in a list.

    >>> index_of_smallest([1,2,3,4,5])
    0
    >>> index_of_smallest([9,8,7,6,4])
    4
    >>> index_of_smallest([])
    -1
    >>> index_of_smallest([4,5,2,6,3,2])
    2
    >>> index_of_smallest(["hello","hi","sup"])
    0
    >>> index_of_smallest(["hi","sup","hello"])
    2
    
    '''

    if (len(lst) == 0 ):
        return -1
    
    holder = [lst[0],0]

    for num in range (1,len(lst)):
        if lst[num] < holder[0]:
            holder[0] = lst[num]
            holder[1] = num

    return holder[1]

def total_duration(flight_list:list[Flight])->float:
    '''
    returns the total durations of all flights in a list.

    >>> total_duration([("Prince Rupert","Vancouver",1.5), ("Vancouver", "Victoria", 0.5)])
    2.0

    >>> total_duration([("Prince Rupert","Vancouver",1.5), ("Vancouver", "Victoria", 0.5), ("a","b",15.9)])
    17.9

    >>> total_duration([])
    0
    
    '''

    total = 0

    if (len(flight_list) == 0):
        return total
    
    for fly in flight_list:
        total += fly[DURATION]

    return total

def get_destinations_from(flight_list:list[Flight],origin:str)->list[str]:
    '''
    takes a list of flights and returns a list of places gone to where the departure is
    the given origin city.

    >>> get_destinations_from([("Prince Rupert","Vancouver",1.5), ("Prince Rupert", "Victoria", 0.5)], "Prince Rupert")
    ['Vancouver', 'Victoria']

    >>> get_destinations_from([("Prince Rupert","Vancouver",1.5), ("Prince Rupert", "Victoria", 0.5),("Prince Rupert", "Victoria", 0.5)], "Prince Rupert")
    ['Vancouver', 'Victoria']

    >>> get_destinations_from([],"Calgary")
    []

    >>> get_destinations_from([("Hanoi","Vancouver",1.5), ("Beijing", "Victoria", 0.5),("Hanoi", "Victoria", 0.5)], "Prince Rupert")
    []

    >>> get_destinations_from([("Hanoi","Vancouver",1.5), ("Beijing", "Victoria", 0.5),("Hanoi", "Victoria", 0.5)], "Hanoi")
    ['Vancouver', 'Victoria']
    
    '''
    arrived = []
    if (len(flight_list) == 0):
        return arrived
    
    for fly in flight_list:
        if (fly[DEPARTURE] == origin and (fly[ARRIVAL] not in arrived)):
            arrived.append(fly[ARRIVAL])

    return arrived