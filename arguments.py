import argparse


def set_up_argparse() -> argparse.ArgumentParser:
	"""Sets up arguments for argparse package

	Returns:
			argparse.ArgumentParser: a set-up argument parser object
	"""
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
	"""Parses passed in arguments

	Args:
			parser (argparse.ArgumentParser): parser object

	Returns:
			argparse.Namespace: namespace containing the arguments
	"""
	args, _ = parser.parse_known_args()
	return args


def get_width(args: argparse.Namespace) -> int:
	"""Gets the width of the board

	Args:
			args (argparse.Namespace): argument namespace

	Returns:
			int: the passed in width, defaults to 10
	"""
	return args.width if (args.width is not None) else 10


def get_height(args: argparse.Namespace) -> int:
	"""Gets the height of the board

	Args:
			args (argparse.Namespace): argument namespace

	Returns:
			int: the passed in height, defaults to 10
	"""
	return args.height if (args.height is not None) else 10


def get_words(args: argparse.Namespace) -> str:
	"""Gets the path to the file containing words to use

	Args:
			args (argparse.Namespace): argument namespace

	Returns:
			str: path to word file, defaults to "./words.txt"
	"""
	return args.word_list if (args.word_list is not None) else './words.txt'


def get_num_of_words(args: argparse.Namespace) -> int:
	"""Gets the number of words to limit the board to

	Args:
			args (argparse.Namespace): argument namespace

	Returns:
			int: maximum number of words to include, defaults to 5
	"""
	return args.number if (args.number is not None) else 5
