import argparse


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


def get_width(args: argparse.Namespace) -> int:
	return args.width if (args.width is not None) else 10


def get_height(args: argparse.Namespace) -> int:
	return args.height if (args.height is not None) else 10


def get_words(args: argparse.Namespace) -> str:
	return args.word_list if (args.word_list is not None) else './words.txt'


def get_num_of_words(args: argparse.Namespace) -> int:
	return args.number if (args.number is not None) else 5
