# taken from my tic tac toe tkinter implementation

def minimax(self, depth, is_maximizing):
    winner = self.find_winner()
    if winner == self.cpu:
        return 10 - depth
    elif winner == self.player:
        return depth - 10
    elif self.is_draw():
        return 0

    if is_maximizing: # cpu move
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = self.cpu # try a move
                    score = self.minimax(depth + 1, False) # recursion
                    self.board[i][j] = ""  # undo the move
                    best_score = max(score, best_score)
        return best_score
    else: # user move
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = self.player
                    score = self.minimax(depth + 1, True)
                    self.board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score