import os
import math

file = open('input.txt')
inputs = file.read().split('\n')

####################### part 1 ############################

cube_pool = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def possible_game_1(game, cube_pool):
    game_id = int(game.split(':')[0].split(' ')[-1])
    stop = False
    for cube_ss in game.split(': ')[-1].split('; '):
        for color in cube_ss.split(', '):
            n,c = color.split(' ')
            if int(n) > cube_pool[c]:
                possible = 1
                stop = True
                break
        if stop:
            return 0
    return game_id

def part1(inputs, cube_pool):
    return sum([possible_game_1(game,cube_pool) for game in inputs])

print(part1(inputs, cube_pool))


####################### part 2 ############################

'''
Solution works fine because in every game all colors and picked at least once
If not, before calculating the product, would have needed to remove the 0 values

'''

def game_2(game):
    needed_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for cube_ss in game.split(': ')[-1].split('; '):
        for color in cube_ss.split(', '):
            n,c = color.split(' ')
            if int(n) > needed_cubes[c]:
                needed_cubes[c] = int(n)

    return math.prod(needed_cubes.values())

def part2(inputs):
    return sum([game_2(game) for game in inputs])

print(part2(inputs))