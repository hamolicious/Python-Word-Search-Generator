
from random import choice, randint, shuffle
import string
import argparse
import os

def generate_grid(w: int, h: int) -> list[list[str]]:
		grid = []
		for _ in range(h):
				row = []
				for _ in range(w):
						row.append(' ')
				grid.append(row)

		return grid


def generate_vel() -> list[int]:
	return choice(
		[
			[0, 1],
			[1, 0],
		]
	)


def generate_pos(w: int, h: int) -> list[int]:
	return [
		randint(0, w),
		randint(0, h)
	]


def add_vec(vec1: list[int], vec2: list[int]) -> list[int]:
	return [
		vec1[0] + vec2[0],
		vec1[1] + vec2[1],
	]


def mult_vec(vec1: list[int], n: int) -> list[int]:
	return [
		vec1[0] * n,
		vec1[1] * n
	]


def generate_mask_from_grid(grid: list[list[str]]) -> list[list[int]]:
	mask = []

	for row in grid:
		mask_row = []
		for _ in row:
			mask_row.append(0)
		mask.append(mask_row)

	return mask


def populate_grid_with_random_let(grid: list[list[str]]) -> list[list[str]]:
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == ' ':
				grid[i][j] = choice(string.ascii_uppercase)

	return grid


def populate_grid_with_words(words: list[str], grid: list[list[str]]) -> list[list[str]]:
	# HACK: need to think of a better algo to generate the words
	mask = generate_mask_from_grid(grid)
	shuffle(words)
	width, height = len(grid), len(grid[0])
	attempts = 1000
	added_words = []

	for word in words:
		valid = True
		for _ in range(attempts):
			pos = generate_pos(width, height)
			vel = generate_vel()

			end_point = add_vec(pos, mult_vec(vel, len(word)))
			if end_point[0] < 0 or end_point[0] >= width\
				or end_point[1] < 0 or end_point[1] >= height:
				valid = False

			if not valid:
				continue

			temp_pos = pos.copy()
			for l in word:
				mask_char = mask[temp_pos[1]][temp_pos[0]]
				if not (mask_char == 0 or mask_char == l):
					valid = False
					break
				temp_pos = add_vec(temp_pos, vel)

			if not valid:
				continue

			for l in word:
				grid[pos[1]][pos[0]] = l
				mask[pos[1]][pos[0]] = l

				pos = add_vec(pos, vel)

			added_words.append(word)
			break

	if len(added_words) != len(words):
		return populate_grid_with_words(words, generate_grid(width, height))

	return grid


def str_grid(grid: list[list[str]]) -> list[list[str]]:
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			grid[i][j] = str(grid[i][j])
	return grid


def draw_grid(grid: list[list[str]], used_words: list[str]) -> None:
	grid = str_grid(grid)
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
				output.append(words[0].upper())
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
grid = populate_grid_with_words(words, grid)
grid = populate_grid_with_random_let(grid)

clear()
draw_grid(grid, words)

