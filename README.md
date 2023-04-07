# Roman Numeral Converter

This program is a Python implementation of a Roman numeral converter, which can convert integers to Roman numerals and vice versa.

## Usage

To use the program, simply run the `main()` function. The program will prompt the user to choose between two conversion options:

- Convert an integer to a Roman numeral
- Convert a Roman numeral to an integer

After selecting an option, the user will be prompted to enter the number or numeral they would like to convert. If the input is valid, the program will output the converted value. If the input is not valid, the program will display an error message and prompt the user to try again.

## Implementation

The program is implemented using a class called `RomanNumeralConverter`. The class contains two class methods:

- `to_roman(cls, n: int) -> str`: Convert an integer to a Roman numeral
- `from_roman(cls, s: str) -> int`: Convert a Roman numeral to an integer

The `to_roman` method uses a predefined tuple `ROMAN_NUMERAL_MAP` to convert the input integer to a Roman numeral. The method first checks if the input integer is within the valid range (1 to 3999). If the input is not valid, the method raises a `ValueError` exception. Otherwise, the method iterates over the `ROMAN_NUMERAL_MAP` tuple and adds the corresponding numeral to the result string until the input integer is fully converted.

The `from_roman` method does the opposite conversion, i.e., it converts a Roman numeral to an integer. The method first checks if the input string is a valid Roman numeral. If the input is not valid, the method raises a `ValueError` exception. Otherwise, the method iterates over the `ROMAN_NUMERAL_MAP` tuple and adds the corresponding integer to the result until the input string is fully converted.

The `main` function handles the user input and output. It repeatedly prompts the user to choose an option and enter a valid input until the user chooses to exit.

## Limitations

The program has some limitations, such as:

- It only supports Roman numerals up to 3999 which is all that Roman Numerals actually support.
- It does not support lowercase Roman numerals.
- It does not support the overline notation for Roman numerals.

## Acknowledgments

The implementation of the `RomanNumeralConverter` class is inspired by the algorithm described in the [Roman numeral Wikipedia page](https://en.wikipedia.org/wiki/Roman_numerals).
