       
def print_fat_cat():
    '''
    Prints a sleepy fat cat.
    '''
    print("   ^--^       Z")
    print("\"( -  - )\" ^ z")
    print("( U    U ) \\\\")
    print("(        )=//")
    print(" U\'----\'U")

def print_fast_snail():
    '''
    Prints a really fast snail. He's a little flat.
    '''
    print("         ___________")
    print("       /             \\")
    print("      (               )")
    print(" @ @ (                 )")
    print(" |_| (                 ) '")
    print("  \ \ \\_____     _____/ \"")
    print("   C _________________  / -  -  - zoom ")

def print_logo():
    '''
    Prints logo of a fat cat and fast snail.
    '''
    print("/~~~~~~~~\\")
    print_fat_cat()
    print("/~~~~~~~~\\")
    print_fast_snail()
    print("/~~~~~~~~\\")
    print_fat_cat()
    print("/~~~~~~~~\\")
    print_fast_snail()
    print("/~~~~~~~~\\")
     
def calculate_surface_area(height:float, diameter:float):
    '''
    When given the height and diameter of a cylinder,
    it will print out the surface area of the cylinder.
    >>> calculate_surface_area(1.2,3.5)
    32.4
    >>> calculate_surface_area(4.1,4.3)
    84.4
    '''
    II = 3.14
    circumference = II*(diameter)
    top_area = II*(diameter/2)**2
    wrapped_area = circumference*height
    total_area = wrapped_area+(2*top_area)
    print(f'cylinder area: {total_area:.1f}')

