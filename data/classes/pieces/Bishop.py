import pygame

from data.classes.Piece import Piece

class Bishop(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		img_path = 'data/imgs/' + color[0] + '_bishop.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

		self.notation = 'B'


	def get_possible_moves(self, board):
		"""
		Inputs: board (Board object)
		Outputs: list of lists of Square objects

		Returns a list of lists of Square objects, where each list of Square objects represents a possible direction of movements for the Bishop.
		Example:
		[
			[Square(0, 0), Square(0, 1), Square(0, 2), Square(0, 3), Square(0, 4), Square(0, 5), Square(0, 6), Square(0, 7)], # North
			[Square(1, 7), Square(2, 7), Square(3, 7), Square(4, 7), Square(5, 7), Square(6, 7), Square(7, 7)], # East
			[Square(7, 6), Square(7, 5), Square(7, 4), Square(7, 3), Square(7, 2), Square(7, 1), Square(7, 0)], # South
			[Square(6, 0), Square(5, 0), Square(4, 0), Square(3, 0), Square(2, 0), Square(1, 0)] # West
		]

		"""
		# TODO: The Bishop can move any number of squares diagonally.
		output = []

		valid_move = self.get_valid_moves(board)
		valid_pos = [(each_square.x, each_square.y) for each_square in valid_move]
		directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

		for each_direction in directions:
			current_direction = []
			new_x = self.x + each_direction[0]
			new_y = self.y + each_direction[1]

			while new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
				if (new_x, new_y) in valid_pos:
					current_direction.append(board.get_square_from_pos((new_x, new_y)))
			
			output.append(current_direction)

		return output
