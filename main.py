
from random import choice, randint
import os

def generate_grid(w, h):
    global width, height
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'

    grid = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(' ')
        grid.append(row)

    return grid

def populate_grid(words, grid):
    for word in words:
        done = False
        tries = 10
        while not done:
            try:
                start_x = randint(0, len(grid[0]) - len(word))
                start_y = randint(0, len(grid) - len(word))
                vel = choice([(1, 0), (0, 1), (1, 1)])
            except ValueError:
                done = True
                break

            valid_spot = True
            x, y = start_x, start_y
            for i in range(len(word)):
                if grid[y][x] == ' ' or grid[y][x] == word[i]:
                    pass
                else:
                    valid_spot = False
                    tries -= 1
                    break

                x += vel[0]
                y += vel[1]

            if tries <= 0:
                done = True

            if valid_spot:
                x, y = start_x, start_y
                for i in range(len(word)):
                    grid[y][x] = word[i].upper()
                    x += vel[0]
                    y += vel[1]
                done = True

    alphabet = 'qwertyuiopasdfghjklzxcvbnm'.upper()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ' ':
                grid[i][j] = choice(alphabet)

    return grid

def draw_grid(grid):
    screen = ''

    for row in grid:
        screen += '\n'
        do_once = True
        for tile in row:
            if do_once:
                screen += '|'
                do_once = False
            screen += tile + '|'

    print(screen)

def use_random():
    path = 'words.txt'
    if os.path.exists(path):
        with open(path, 'r') as file:
            temp = file.readlines()

        class wrd():
            def __init__(self, word):
                self.word = word
                self.index = randint(0, 1000)

            def __lt__(self, other):
                return self.index < other.index

        words = []
        word_count = 5
        for word in temp:
            w = word.replace('\n', '')
            words.append(wrd(w))
        words.sort()

        temp = []
        for i in range(word_count):
            temp.append(words[i].word)

        return temp

def get_details():
    # width
    while True:
        w = input('\nWhat is the width of the grid in characters?\n[>> ')
        if w.isdigit():
            w = int(w)
            break

    # height
    while True:
        h = input('\nWhat is the height of the grid in characters?\n[>> ')
        if h.isdigit():
            h = int(h)
            break

    # words
    words = []
    while True:
        wrd = input('Please add the words to the bank, you can press ENTER to use random words and press "q" when you\'re finished.\n[>> ').strip().lower()

        if wrd == '':
            words = use_random()
            break

        if wrd == 'q':
            break

        for let in wrd:
            if let not in 'qwertyuiopasdfghjklzxcvbnm':
                print('Invalid word, words can only contain the following letters:', ''.join(i for i in sorted('qwertyuiopasdfghjklzxcvbnm')))
                break
        else:
            words.append(wrd)

    return w, h, words

def clear():
    print('\n' * 50)

width, height, words = get_details()

while True:
    grid = generate_grid(width, height)
    grid = populate_grid(words, grid)

    clear()
    draw_grid(grid)

    input('>')






































