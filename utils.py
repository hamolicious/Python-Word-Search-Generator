from random import choice, randint


def clear() -> None:
	"""Basic way of clearing the screen
	"""
	print('\n' * 50)


def str_grid(grid: list[list[str]]) -> list[list[str]]:
	"""Strigifies all cells in the grid

	Args:
			grid (list[list[str]]): 2d array representing the grid

	Returns:
			list[list[str]]: 2d array representing the grid where every cell is cast to a string
	"""
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			grid[i][j] = str(grid[i][j])
	return grid


def generate_vel() -> list[int]:
	"""Generates a random velocity (direction) from a list

	Returns:
			list[int]: 2d vector showing a direction
	"""
	return choice(
		[
			[0, 1],
			[1, 0],
		]
	)


def generate_pos(w: int, h: int) -> list[int]:
	"""Generates a 2d vector within a bounding box (0-w,0-h)

	Args:
			w (int): width
			h (int): height

	Returns:
			list[int]: 2d vector inside the bounding box
	"""
	return [
		randint(0, w),
		randint(0, h)
	]


def add_vec(vec1: list[int], vec2: list[int]) -> list[int]:
	"""Adds 2 vectors together

	Args:
			vec1 (list[int]): vec a
			vec2 (list[int]): vec b

	Returns:
			list[int]: sum of vector a and b
	"""
	return [
		vec1[0] + vec2[0],
		vec1[1] + vec2[1],
	]


def mult_vec(vec1: list[int], n: int) -> list[int]:
	"""Multiplies a vector by a number

	Args:
			vec1 (list[int]): vec a
			n (int): number to multiply the vector by

	Returns:
			list[int]: 2d vector scaled to n
	"""
	return [
		vec1[0] * n,
		vec1[1] * n
	]
