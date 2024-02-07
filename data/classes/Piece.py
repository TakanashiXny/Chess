import pygame

class Piece:
	def __init__(self, pos, color, board):
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.color = color
		self.has_moved = False


	def move(self, board, square):
		"""
		Inputs board, square
		Outputs: boolean

		Move the piece to the square if it is a valid move. Return True if the move is successful, False otherwise.
		"""
		# Unhighlight all squares
		for i in board.squares:
			i.highlight = False
		if square in self.get_valid_moves(board):
			# TODO: Move the piece to the square if it is a valid move. Update the state of the board. Return True if the move is successful, False otherwise.
			x = square.x
			y = square.y
			# square.occupying_piece = self
			
			# Update the destination square
			board.squares[y*8+x].occupying_piece = self
			board.squares[self.y*8+self.x].occupying_piece = None # Update the original square
			return True
		else:
			board.selected_piece = None
			return False


	def get_moves(self, board):
		"""
		Inputs: board
		Outputs: list of squares that the piece can move to

		For each direction, get all squares until a piece is encountered.
		If the piece is of the same color, stop. If the piece is of the opposite color, include the square and stop.
		"""
		# TODO: Gets all moves for the piece. That is, all squares that the piece can move to.
		# HINT: First get all squares in each direction, then filter out the invalid ones based on if an opposite color piece is in the way.
		output = []

		# Get all squares in each direction
		directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

		for each_direction in directions:
			new_x = self.x + each_direction[0]
			new_y = self.y + each_direction[1]

			while new_x >= 0 and new_x < 8 and new_y >= 0 and new_y < 8:
				new_pos = (new_x, new_y)
				occupying_piece = board.get_piece_from_pos(new_pos)
				if occupying_piece is None:
					output.append(board.get_square_from_pos(new_pos))
				elif occupying_piece.color == self.color:
					break
				else:
					output.append(board.get_square_from_pos(new_pos))
					break
					
				new_x += each_direction[0]
				new_y += each_direction[1]

		return output


	def get_valid_moves(self, board):
		"""
		Inputs: board
		Outputs: list of squares that the piece can move to without putting the king in check

		For each square that the piece can move to, check if the king is in check after the move.
		"""
		# TODO: A move is valid if it does not put this king in check
		# HINT: Gets all moves for the piece, then filters out the ones that put the king in check.
		output = []

		all_moves_dest = self.get_moves(board)
		all_moves = [((self.x, self.y), (each_moves_dest.x, each_moves_dest.y)) 
			   for each_moves_dest in all_moves_dest]

		output = [board.get_square_from_pos(each_move[1]) 
			for each_move in all_moves if not board.is_in_check(self.color, each_move)]

		return output


	# True for all pieces except pawn
	def attacking_squares(self, board):
		"""
		Inputs: board
		Outputs: list of squares that the piece is attacking

		For each direction, get all squares until a piece is encountered.
		"""
		return self.get_moves(board)