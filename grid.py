import os
import string
from random import choice, shuffle

import utils


def generate_grid(w: int, h: int) -> list[list[str]]:
		grid = []
		for _ in range(h):
				row = []
				for _ in range(w):
						row.append(' ')
				grid.append(row)

		return grid


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
			pos = utils.generate_pos(width, height)
			vel = utils.generate_vel()

			end_point = utils.add_vec(pos, utils.mult_vec(vel, len(word)))
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
				temp_pos = utils.add_vec(temp_pos, vel)

			if not valid:
				continue

			for l in word:
				grid[pos[1]][pos[0]] = l
				mask[pos[1]][pos[0]] = l

				pos = utils.add_vec(pos, vel)

			added_words.append(word)
			break

	if len(added_words) != len(words):
		return populate_grid_with_words(words, generate_grid(width, height))

	return grid


def draw_grid(grid: list[list[str]], used_words: list[str]) -> None:
	grid = utils.str_grid(grid)
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

