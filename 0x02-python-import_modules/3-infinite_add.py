#!/usr/bin/python3
import sys


def infinite_sum():
    arguments = sys.argv
    nums = arguments[1:]
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    print(sum(nums))

if __name__ == "__main__":
    infinite_sum()
