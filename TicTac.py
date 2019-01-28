class Game:
	def __init__(self):
		self.current_turn = 0
		self.current_symbol = None
		self.game_board = {}
		self.winning_numbers = [set("123"), set("456"), set("789"), set("159"), set("357")]
		self.xMoves = set()
		self.oMoves= set()
		self.activeSet = None
	def board(self):
		i = 1
		board = self.game_board
		while i != 10:
			board['{}'.format(i)] = "-"
			i+=1
			if i == 10: break
		print("I ran")
		return board
	def print_board(self):
		board = self.game_board
		print("{}|{}|{}".format(board["1"], board["2"], board["3"]),
		 "{}|{}|{}".format(board["4"], board["5"], board["6"]), "{}|{}|{}".format(board["7"], board["8"], board["9"]), sep='\n')
		return board


	def change_turn(self):
		if self.current_turn % 2 == 0:
			self.current_symbol = "X"
			self.activeSet = self.xMoves
		else:
			self.activeSet = self.oMoves
			self.current_symbol = "O"

	def get_input(self):
		user_move = -1
		print("User entered: {}".format(user_move))
		while int(user_move) not in range(1, 10):
			user_move = input("From 1-9 where do you want to place your symbol?")
			if user_move == "":
				user_move = "-1"
		return user_move
	def check_win(self):
		i = 0
		while len(self.winning_numbers) > i:
			check = self.winning_numbers[i] - self.activeSet
			if len(check) == 0:
				print("{} Wins".format(self.current_symbol))
				return True
			i+=1
		return False
	def game(self):
		self.board()
		while 9 != self.current_turn:
			board = self.print_board()
			self.change_turn()
			print("Current turn is to {}".format(self.current_symbol))
			print("current turn is {}".format(self.current_turn))
			user_input = self.get_input()
			print("{}".format(board[user_input]))
			if board[user_input] != "-":
				print("Occupied")
			else:
				board[user_input] = self.current_symbol
				self.activeSet.add(user_input)
				self.print_board()
				check = self.check_win()
				if check:
					break
				elif check == False:
					print("No winners")
				self.current_turn+=1
				self.change_turn()
def main():
	game = Game()
	game.game()
if __name__ == '__main__': main()