import pygame

from data.classes.Piece import Piece

class Pawn(Piece):
	def __init__(self, pos, color, board):
		super().__init__(pos, color, board)

		img_path = 'data/imgs/' + color[0] + '_pawn.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.tile_width - 35, board.tile_height - 35))

		self.notation = ' '


	def get_possible_moves(self, board):
		"""
		Inputs: board (Board object)
		Outputs: list of lists of Square objects

		On the first move, a Pawn can move forward two squares. On all other moves, a Pawn can only move forward one square.

		Returns a list of lists of Square objects, where each list of Square objects represents a possible direction of movements for the Pawn.
		Example:
		[
			[Square(0, 0), Square(0, 1), Square(0, 2), Square(0, 3), Square(0, 4), Square(0, 5), Square(0, 6), Square(0, 7)], # North
			[Square(1, 7), Square(2, 7), Square(3, 7), Square(4, 7), Square(5, 7), Square(6, 7), Square(7, 7)], # East
			[Square(7, 6), Square(7, 5), Square(7, 4), Square(7, 3), Square(7, 2), Square(7, 1), Square(7, 0)], # South
			[Square(6, 0), Square(5, 0), Square(4, 0), Square(3, 0), Square(2, 0), Square(1, 0)] # West
		]

		"""
		# TODO: The Pawn can move forward two squares on its first move, and one square on all other moves.
		output = []
		return output


	def get_moves(self, board):
		"""
		Inputs: board
		Outputs: list of squares that the pawn can move to

		Overrides the get_moves method in the Piece class. Returns a list of squares that the Pawn can move to.
		"""
		# TODO: Gets all moves for the piece. That is, all squares that the piece can move to.
		# HINT: First get all squares in each direction using get_possible_moves, then filter out the invalid ones.
		output = []
		return output

	def attacking_squares(self, board):
		"""
		Inputs: board (Board object)

		Returns a list of squares that the Pawn can attack.
		"""
		moves = self.get_moves(board)
		# return the diagonal moves 
		return [i for i in moves if i.x != self.x]