from random import choice, randint


def clear() -> None:
		print('\n' * 50)


def str_grid(grid: list[list[str]]) -> list[list[str]]:
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			grid[i][j] = str(grid[i][j])
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
