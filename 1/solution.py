import os
import re

file = open('input.txt')
inputs = file.read().split('\n')

####################### part 1 ############################

'''
Naive solution
Simply look for first and last occurence of a digit
'''

numlist = '0123456789'

sumcv = 0

for word in inputs:
    cv = ''
    for felem in word:
        if felem in numlist:
            cv+= felem
            break
    for belem in word[::-1]:
        if belem in numlist:
            cv+= belem
            break

    sumcv += int(cv)

print(sumcv)

sols = {}

####################### part 2 ###########################

'''
Regex replacement does not work
e.g 13twotwonec
intended: 13221c
regex:1322nec

have to iteratively look at substrings
'''

digits_dict = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }


sumcv = 0

for word in inputs:
    cv = ''
    for i in range(len(word)):
        for digit in digits_dict.keys():
            if word[i:].startswith(digit):
                cv += digits_dict[digit]
                break
    sumcv += int(cv[0] + cv[-1])

print(sumcv)