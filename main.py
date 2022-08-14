
from random import choice, randint, shuffle
import string
import argparse
from sys import argv
import os
from typing import Any


def generate_grid(w: int, h: int) -> list[list[str]]:
		grid = []
		for _ in range(h):
				row = []
				for _ in range(w):
						row.append(' ')
				grid.append(row)

		return grid


def populate_grid(words: list[str], grid: list[list[str]]) -> list[list[str]]:
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

		alphabet = string.ascii_uppercase
		for i in range(len(grid)):
				for j in range(len(grid[0])):
						if grid[i][j] == ' ':
								grid[i][j] = choice(alphabet)

		return grid


def draw_grid(grid: list[list[str]], used_words: list[str]) -> None:
		used_words = iter(used_words)
		pipe = '|'

		screen = f'{pipe}{pipe.join(grid[0])}{pipe}'
		line_len = len(screen.split('\n')[-1])
		screen = ''
		print(f'{" " * line_len}\tWords to Find:')

		for row in grid:
			try:
				word = next(used_words)
			except StopIteration:
				word = ''
			screen += f'\n{pipe}{pipe.join(row)}{pipe}\t{word}'

		print(screen)
		while True:
			try:
				word = next(used_words)
				print(f'{" " * line_len}\t{word}')
			except StopIteration:
				break


def use_random(path: str, num_words: int) -> list[str]:
		output = []

		if os.path.exists(path):
			with open(path, 'r') as file:
					words = file.read().split('\n')

			for _ in range(num_words):
				shuffle(words)
				output.append(words[0])
				words.remove(words[0])

				if len(words) == 0:
					break

			return output

		else:
			raise FileNotFoundError(
				f'file ({path}) cannot be found'
			)


def set_up_argparse() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser()

	parser.add_argument(
		'-w', '--width',
		help='Defines the width of the board, defaults to 10',
		type=int,
	)
	parser.add_argument(
		'-e', '--height',
		help='Defines the height of the board, defaults to 10',
		type=int
	)
	parser.add_argument(
		'-n', '--number',
		help='Used for huge text lists, sets the maximum number of words that will be used, defaults to 5',
		type=int
	)
	parser.add_argument(
		'-l', '--word-list',
		help='Points to a word list to use the words from, defaults to "./words.txt"',
		type=str
	)

	return parser


def parse_args(parser: argparse.ArgumentParser) -> argparse.Namespace:
	args, _ = parser.parse_known_args()
	return args


def get_width() -> int:
	return args.width if (args.width is not None) else 10


def get_height() -> int:
	return args.height if (args.height is not None) else 10


def get_words() -> str:
	return args.word_list if (args.word_list is not None) else './words.txt'


def get_num_of_words() -> int:
	return args.number if (args.number is not None) else 5


def clear() -> None:
		print('\n' * 50)


parser = set_up_argparse()
args = parse_args(parser)
width = get_width()
height = get_height()
path_word_list = get_words()
num_words = get_num_of_words()

grid = generate_grid(width, height)
words = use_random(path_word_list, num_words)
grid = populate_grid(words, grid)

clear()
draw_grid(grid, words)

