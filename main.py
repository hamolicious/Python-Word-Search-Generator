
import arguments
import grid as grid_utils
import utils

parser = arguments.set_up_argparse()
args = arguments.parse_args(parser)
width = arguments.get_width(args)
height = arguments.get_height(args)
path_word_list = arguments.get_words(args)
num_words = arguments.get_num_of_words(args)

grid = grid_utils.generate_grid(width, height)
words = grid_utils.use_random(path_word_list, num_words)
grid = grid_utils.populate_grid_with_words(words, grid)
grid = grid_utils.populate_grid_with_random_let(grid)

utils.clear()
grid_utils.draw_grid(grid, words)

