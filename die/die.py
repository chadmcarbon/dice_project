from random import randint

class Die:
    """
    This Die Class has a default attribute called sides with a value of 6. It 
    includes a method, roll_die() that prints a random number between 1 and the 
    number of sides the die has.

    Attributes:
        sides: The number of sides the die has.
    """

    def __init__(self):
        """ 
        Initialize attributes with a new instance.

        Parameters:
            sides: The number of sides a die has.
        """
        self.sides = 6

    def roll_die(self):
        """
        This method simulates rolling a die between 1 and the number of sides
        the die has 10 times.
        """
        print('Rolling the 6-sided die 10 times: ')
        for num in range(1, 11):
            print(
                f" Roll {num}: {randint(1, self.sides)}"
            )

class TenSideDie(Die):
    """
    This class is a child class of the Die Class. It includes a roll die 
    method that overrides the six sided method in the parent class.

    Attributes:
        sides: The number of sides the die has.
    """

    def __init__(self):
        """
        Initialize attributes of the parent class.
        """
        super().__init__()
        self.sides = 10

    
    def roll_die(self):
        """
        This method simulates rolling a 10 sided die 10 times
        """
        print("\n")
        print('Now rolling the 10-sided die 10 times ...')
        for num in range(1, 11):
            print(
                f" Roll {num}: {randint(1, self.sides)}"
            )


