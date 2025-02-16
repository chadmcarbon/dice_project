# Dice Project

A simple dice simulation program built in Python.

## Project Structure

```plaintext
dice_project/
├── README.md         # Project Documentation
├── die/              # Contains modules for die functionality
│   ├── __init__.py   # Package initializer
│   └── die.py        # Defines the Die class and related methods
└── main.py           # Entry point of the application
```

## Description

The dice_project simulates the roll of a die. The main program (`main.py`) 
utilizes methods from the `die` module (`die.py`) located in the `die` folder 
to generate random dice rolls.

## Features

- Rolls a 6-sided die and displays the outcome.
- Rolls a 10-sided die and displays the outcome.
- Demonstrates modular code with separate files for different functionalities.

## Prerequisites

- Python 3.x installed on your system.

## Additional Documentation

### Class Overview

- **Die:**

    A class representing a standard 6-sided die. 
    
    It includes the `roll_die()` method, which simulates rolling the die 
    10 times and printing each outcome.

- **TenSidedDie:**
    
    A subclass of `Die` that represents a 10-sided die. 
    
    It overrides the `roll_die()` method to simulate rolling the 10-sided 
    die 10 times and printing each outcome.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/dice_project.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd dice_project
   ```

3. **Run the program:**

   ```bash
   python main.py
   ```

## Usage

When you run the program, it will simulate a die roll and print the result to 
the console. Feel free to modify `die/die.py` to adjust the behavior or add new 
features.

## Contributing

If you wish to contribute, please fork the repository and submit a pull 
request. For major changes, open an issue first to discuss what you’d like to 
modify.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file 
for details. 

## Source Code

### main.py

```python
#!/usr/bin/env python3
"""
This program imports the Die Class from the die.py module, creates an instance 
of the die, and calls the method that prints the rolled numbers.
"""
from die.die import Die, TenSideDie

def main():

    #  Create an instance of the Die Class and call roll die method
    my_die = Die()
    my_die.roll_die()

    # Create instance of the TenSided Die Class and call overridden method
    my_new_die = TenSideDie()
    my_new_die.roll_die()

if __name__ == '__main__':
    main()
```

### dice/die.py
```python
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
```

### die/__init__.py
```python
# This file makes the ‘die’ directory a Python package.
```