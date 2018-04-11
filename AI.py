#!/usr/bin/python
class AI:
	def __init__(self, player):
		self.player = player
	def choose_piece(self, board, pieces, opponents):
		'''
		By whatever criteria you choose, select a piece to move. You will need to return the piece and its available jumps		
		'''
		jumps = []
		all_pieces = pieces + opponents
		piece = ''
		squares = board.get_squares()
		for p in pieces:
			if p.alive:
				jump = False
				for r in pieces:
					jumps = r.check_jump(all_pieces,squares)
					if not jumps == []:
						jump = True
						piece = r
						moves = r.check_jump(all_pieces,squares)
						return (piece, moves)
				if not jump:
					add = True
					moves =  p.get_possibilities(squares)
					if not moves == []:
						for m in moves:
							c = board.get_square_coord(m)
							if c is not None:
								for a in all_pieces:
									if a.alive and a.col == c.col and a.row == c.row:
										add = False
								if add:
									add = True
									piece = p
									return (piece, moves)

	
	def move_piece(self,piece,board,pieces,opponents):
		'''
		Move the piece to its new location
		'''
		squares = board.get_squares()
		moves = piece.get_possibilities(squares)
		jumps = piece.check_jump(pieces + opponents,squares)
		move = moves[0]
		m = board.get_square_coord(move)
		#move the piece
		if not jumps == []:
			jump = jumps[0]
			piece.move(jump['position'][0],jump['position'][1])
			jump['piece'].alive = False
			jumps = piece.check_jump(pieces + opponents, squares)
		else:
			piece.move(m.col, m.row)
		return (piece,jumps,pieces,opponents)