import doctest
from race_time import RaceTime
from race_result import RaceResult

# represents a racer as (name, country)
# where name and country != ''
RacerNameCountry = tuple[str, str]

# columns of values in input file row and positions in RacerNameCountry
NAME = 0
COUNTRY = 1
TIME_MS = 2

MIN = 0
SEC = 1
MS = 2

def convert_time(data:str)-> list[int]:
    '''
    when given a string in milliseconds, returns the value as minutes,
    seconds, and miliseconds in a list.

    >>> convert_time('473640')
    [7, 53, 640]

    >>> convert_time('0')
    [0, 0, 0]

    >>> convert_time('61000')
    [1, 1, 0]
    '''

    time = int(data)
    mins = 0
    secs = 0
    ms = 0
    
    while(time >= 60000):
        time -= 60000
        mins += 1

    while(time >= 1000):
        time -= 1000
        secs += 1

    ms = time
    return [mins,secs,ms]


def read_file(filename: str) -> list[RaceResult]:
    """ returns a list of RaceResults populated with data from filename
    Precondition: the file exists, is not empty, has the following
      information on each row separated by commas:
      racer's name, racer's country, race time in milliseconds>=0
      and contains a header row with the column titles.
      The header row is ignored.

    >>> read_file('0lines_data.csv')
    []
    >>> read_file('9lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Evan Jager', 'United States', RaceTime(450, 0, 8)), \
     RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7)), \
     RaceResult('Saif Saaeed Shaheen', 'Qatar', RaceTime(630, 53, 7)), \
     RaceResult('Wander Moura', 'Brazil', RaceTime(410, 14, 8)), \
     RaceResult('Mahiedine Mekhissi-Benabbad', 'France', RaceTime(90, 0, 8)), \
     RaceResult('Peter Renner', 'New Zealand', RaceTime(50, 14, 8))]
    """
    file_handle = open(filename,'r')
    file_handle.readline()
    races = []

    for line in file_handle:
        line = line.strip()
        info =  line.split(',')
        time = convert_time(info[TIME_MS])
        rt = RaceTime(time[MS],time[SEC],time[MIN])
        race = RaceResult(info[NAME],info[COUNTRY],rt)
        races.append(race)

    return races

def find_athlete(loresults: list[RaceResult], name: str) -> int:
    """ returns the position of RaceResult with given athlete name in loresults
    Returns -1 if name not found
    Returns the position of the first if there >1 RaceResult with given name
    Precondition: case sensitive (ie. 'Brad' != 'brad')

    >>> find_athlete([], 'Brimin Kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))],\
        'brimin kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Brimin Kipruto')
    1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Peter Renner')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Usain Bolt', 'Canada', RaceTime(1, 2, 2019))], \
        'Usain Bolt')
    0
    """
    count = -1
    
    for race in loresults:
        count += 1
        if race.get_name() == name:
            return count
    
    return -1
def get_all_from_country(loresults: list[RaceResult], country: str
                         ) -> list[RaceResult]:
    """ returns a list of all results of the given country
    Precondition: case sensitive (ie. 'Canada' != 'canada')

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 12)), \
     RaceResult('Perrier', 'France', RaceTime(1, 23, 18)), \
     RaceResult('Perrieruels', 'Canada', RaceTime(3, 29, 0)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country([], 'Jamaica')
    []

    >>> get_all_from_country(results, 'jamaica')
    []

    >>> get_all_from_country(results, 'Jamaica') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country(results, 'Japan')
    []
    """
    in_country = []
    for race in loresults:
        if race.get_country() == country:
            in_country.append(race)

    return in_country


def get_fastest_time(loresults: list[RaceResult]) -> RaceTime:
    """ returns the fastest RaceTime of all finish_times of 
    RaceResult instances in loresults
    Precondition: loresults is not empty

    >>> one_result = [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 9))]
    >>> results = \
    [RaceResult('Allen', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 16, 17)), \
     RaceResult('Barnes', 'Canada', RaceTime(3, 43, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 29, 9)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 48, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 17))]

    >>> get_fastest_time(one_result)
    RaceTime(12, 31, 9)
    >>> get_fastest_time(results)
    RaceTime(3, 29, 9)
    """
    winner = loresults[0]
    for race in loresults:
        cur_time = race.get_finish_time()
        if cur_time.is_faster(winner.get_finish_time()) == True:
            winner = race

    return winner.get_finish_time()


def get_with_fastest_time(loresults: list[RaceResult]
                          ) -> list[RacerNameCountry]:
    """ returns a list tuples of fastest RaceResults in loresults

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 6)), \
     RaceResult('Barnes', 'Canada', RaceTime(1, 23, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 10, 7)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 15, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 6))]
     
    >>> get_with_fastest_time([])
    []
    >>> get_with_fastest_time(results)
    [('Zhou', 'China'), ('Davis', 'Jamaica')]
    """
    racer_country = []
    if len(loresults) == 0:
        return racer_country
    
    fastest = get_fastest_time(loresults)

    for race in loresults:
        time = race.get_finish_time()
        if time.__eq__(fastest):
            racer_country.append((race.get_name(),race.get_country()))

    return racer_country