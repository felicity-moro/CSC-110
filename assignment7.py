import doctest
Date = tuple[int,int,int]
YEAR = 0
MONTH = 1
DAY = 2

Show = tuple[str,str,list[str],list[str],Date]
TYPE = 0
TITLE = 1
DIRECTORS = 2
ACTORS = 3
SDATE = 4  



def raise_to_power(list1:list[int],list2:list[int])->None:
    ''''
    Raises the values of list1 by its corrosponding value in list2

    >>> list1 = [2,2,2]
    >>> list2 = [2,4,3,5,6]
    >>> empty = []

    >>> raise_to_power(list1,[0,1,2])
    >>> list1
    [1, 2, 4]

    >>> list2 = [2,4,3,5,6]
    >>> raise_to_power(list2,[1,2,3,2])
    >>> list2
    [2, 16, 27, 25, 6]

    >>> list2 = [2,4,3,5,6]
    >>> raise_to_power(list2,[])
    >>> list2
    [2, 4, 3, 5, 6]

    >>> raise_to_power(empty,[2,4,3,5,6])
    >>> empty
    []

    >>> list2 = [2,4,3,5,6]
    >>> raise_to_power(list2,[2,2,2,2,2,2,2,2,2])
    >>> list2
    [4, 16, 9, 25, 36]
    '''
    if (len(list1) == 0):
        return    
    
    for index in range (len(list1)):

        if index < len(list2):
            list1[index] = list1[index]**list2[index]

def create_date(date:str)->Date:
    '''
    Takes a string in form "day-month-year" and returns the 
    string as a Date as a touple

    >>> create_date("23-Aug-05")
    (2005, 8, 23)

    >>> create_date("1-Feb-50")
    (2050, 2, 1)

    >>> create_date("6-Dec-22")
    (2022, 12, 6)
    
    '''
    list_nums = date.split("-")

    year = 2000 + int(list_nums[2])
    day = int(list_nums[0])
    
    smonth = list_nums[1]
    month = 0

    if (smonth == "Jan"):
        month = 1
    elif (smonth == "Feb"):
        month = 2
    elif (smonth == "Mar"):
        month = 3
    elif (smonth == "Apr"):
        month = 4
    elif (smonth == "May"):
        month = 5
    elif (smonth == "Jun"):
        month = 6
    elif (smonth == "Jul"):
        month = 7
    elif (smonth == "Aug"):
        month = 8
    elif (smonth == "Sep"):
        month = 9
    elif (smonth == "Oct"):
        month = 10
    elif (smonth == "Nov"):
        month = 11
    elif (smonth == "Dec"):
        month = 12

    new_date = (year,month,day)
    
    return new_date
        
def create_show(stype:str,stitle:str,sdirectors:str,sactors:str,sdate:str)-> Show:
    '''
    When given arguments for the show type, title, its directors, its actors, and date as string
    function will return a Show tuple.

    >>> create_show('Movie', 'Audrey & Daisy', 'Bonni Cohen:Jon Shenk', \
    '', '23-Sep-16') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Audrey & Daisy', ['Bonni Cohen', 'Jon Shenk'], [], (2016, 9, 23))   

    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David Walliams:Timothy Spall', \
    '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
    ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
    'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
    (2019, 7, 1)) 
    
    '''
    
    directors = sdirectors.split(":")
    if (len(sdirectors) == 0):
        directors = []
    actors = sactors.split(":")
    if (len(sactors) == 0):
        actors = []
    date = create_date(sdate)
    show = (stype,stitle,directors,actors,date)
    return show
    
def get_titles(shows:list[Show])->list[str]:
    '''
    Returns a list of titles when given a list of shows.

    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
     'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
     'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
     ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
      'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_titles(loshows)
    ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']
    '''

    titles = []
    if (len(shows) == 0):
        return titles
    
    for show in shows:
        titles.append(show[TITLE])

    return titles

def is_actor_in_show(show:Show, actor_to_find:str)->bool:
    '''
    Determines whether or not the given actor is in the given show.

    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Justin Bieber')
    False

    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Michael Cera')
    True

    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'MichaEL cerA')
    True
    '''

    for actor in show[ACTORS]:
        if (actor.lower() == actor_to_find.lower()):
            return True
        

    return False

def is_before(date1:Date, date2:Date)->bool:

    if date1[YEAR] < date2[YEAR]:
        return True
    
    if date1[YEAR] > date2[YEAR]:
        return False
    elif date1[MONTH] > date2[MONTH] and date1[YEAR] == date2[YEAR]:
        return False
    elif date1[DAY] >= date2[DAY] and date1[MONTH] == date2[MONTH] and date1[YEAR] == date2[YEAR] :
        return False
    
    return True
    


def count_shows_before_date(shows:list[Show],comp_date:Date)->int:
    '''
    Counts and returns the ammount of shows released before the given date from 
    the given list of Netflix shows.

    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 2, 6)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
     (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
     'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2017, 4, 18))]

    >>> count_shows_before_date(loshows, (2015, 1, 1))
    0

    >>> count_shows_before_date(loshows, (2018, 10, 20))
    3
    '''
    counter = 0

    for show in shows:
        if (is_before(show[SDATE],comp_date)):
            counter += 1
        
    return counter

def get_shows_with_actor(show_list:list[Show], actor:str)->list[Show]:
    '''
    Returns a list of shows that have the given actor in them from the given list of
    shows.

    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_shows_with_actor(loshows, 'Jonah Hill')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21))]

    >>> get_shows_with_actor(loshows, 'jonaH hiLL')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21))]

    >>> get_shows_with_actor(loshows, 'Justin Bieber')
    []
    '''

    shows = []
    for show in show_list:
        if (is_actor_in_show(show,actor)):
            shows.append(show)

    return shows