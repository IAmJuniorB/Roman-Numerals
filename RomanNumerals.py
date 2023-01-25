class RomanNumeralConverter:
    # Initialize the map letters and corresponding values
    def __init__(self):
        self.roman_numeral_map = (('M', 1000),
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
                                 ('I', 1))

    def to_roman(self, n): # To convert a symbol to numerical form. Roman Numerals do not exceed 3,999
        if n > 3_999:
            raise ValueError("Number should be less than or equal to 3,999 as this is the largest representation of numbers in Roman Numerals")
        result = ''
        for numeral, integer in self.roman_numeral_map:
            while n >= integer:
                result += numeral
                n -= integer
        return result


    def from_roman(self, s): # To convert from symbol to numerical
        invalid_numeral_combination = ['IIII','XXXX','CCCC','MMMM','VV','LL','DD'] # list of a few incorrect combinations. Could be incomplete.
        if not all(x in 'MDCLXVI' for x in s) or len(s)>15 or any(x in s for x in invalid_numeral_combination):
            raise ValueError("Invalid Roman Number - Does not exist")
        result = 0
        index = 0
        for numeral, integer in self.roman_numeral_map:
            while s[index:index+len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        if result > 3999:
            raise ValueError("Number should be less than or equal to 3999")
        return result


converter = RomanNumeralConverter()

print(converter.to_roman(3006))
print(converter.from_roman('MMMVIC'))

"""
Feel free to comment any errors in my code
Or if anything could be improve
Happy to take in any advice
"""
