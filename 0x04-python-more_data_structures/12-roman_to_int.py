#!/usr/bin/python3


def roman_to_int(roman_string):
    if (not isinstance(roman_string, str)) or (roman_string is None):
        return 0
    roman_nums = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    sum_ = 0
    if len(roman_string) >= 2:
        for i in range(1, len(roman_string)):
            if roman_nums[roman_string[i - 1]] >= roman_nums[roman_string[i]]:
                    sum_ = sum_ + roman_nums[roman_string[i - 1]]
            else:
                sum_ = sum_ - roman_nums[roman_string[i - 1]]
        sum_ = sum_ + roman_nums[roman_string[-1]]
        return sum_
    else:
        return roman_nums[roman_string[0]]
