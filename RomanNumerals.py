class RomanNumeralConverter:
    """
    Class for converting integers to Roman numerals and vice versa.
    """

    ROMAN_NUMERAL_MAP = (
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    )

    @classmethod
    def to_roman(cls, n: int) -> str:
        """
        Convert an integer to Roman numeral.
        
        Args:
        - n: an integer between 1 and 3999.
        
        Returns:
        - A string representation of the Roman numeral.
        
        Raises:
        - ValueError: if the input integer is not between 1 and 3999.
        """
        if not 1 <= n <= 3999:
            raise ValueError(f"The input integer must be between 1 and 3999. Got {n}.")

        result = ''
        for numeral, integer in cls.ROMAN_NUMERAL_MAP:
            while n >= integer:
                result += numeral
                n -= integer
        return result

    @classmethod
    def from_roman(cls, s: str) -> int:
        """
        Convert a Roman numeral to an integer.
        
        Args:
        - s: a string representation of a Roman numeral.
        
        Returns:
        - An integer representation of the Roman numeral.
        
        Raises:
        - ValueError: if the input string is not a valid Roman numeral.
        """
        invalid_numeral_combinations = ['IIII', 'XXXX', 'CCCC', 'MMMM', 'VV', 'LL', 'DD']
        if not all(x in 'MDCLXVI' for x in s) or len(s) > 15 or any(x in s for x in invalid_numeral_combinations):
            raise ValueError("Invalid Roman numeral.")

        result = 0
        index = 0
        for numeral, integer in cls.ROMAN_NUMERAL_MAP:
            while s[index:index+len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        return result

def main():
    while True:
        try:
            print("Enter 1 to convert from an integer to a Roman numeral.")
            print("Enter 2 to convert from a Roman numeral to an integer.")
            user_choice = int(input("What would you like to do? "))
            if user_choice == 1:
                user_input = int(input("Enter a number between 1 and 3999: "))
                if user_input <= 0 or user_input > 3999:
                    raise ValueError
                print("Roman numeral equivalent:", converter.to_roman(user_input))
            elif user_choice == 2:
                user_input = input("Enter a Roman numeral: ")
                print("Integer equivalent:", converter.from_roman(user_input))
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please try again.")
