from .models import ChessGame
from django.core.exceptions import ObjectDoesNotExist

class Move:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

class Bauer:
    def __init__(self, startRow, startCol, color):
        self.row = startRow
        self.col = startCol
        self.color = color


    def possibleMoves(self, board):

        moves = []

        if self.color == 0:
            print('test')
            if self.row != 7 and board[self.row + 1][self.col] is None:       #nicht am ende und feld davor frei
                moves.append(Move(1, 0))
                if self.row == 1:  #2 vor wenn am start
                    moves.append(Move(2, 0))
            if self.col != 0 and board[self.row + 1][self.col - 1] is not None: #wenn gegnerische Figur ein feld diagonal ist
                if board[self.row + 1][self.col - 1].color == 1:
                    moves.append(Move(1, -1))
            elif self.col != 7 and board[self.row + 1][self.col + 1] is not None:
                if board[self.row + 1][self.col + 1].color == 1:
                    moves.append(Move(1, 1))
        else:
            if self.row != 0 and board[self.row - 1][self.col] is None:       #nicht am ende und feld davor frei
                moves.append(Move(-1, 0))
                if self.row == 6:  #2 vor wenn am start
                    moves.append(Move(-2, 0))
            if self.col != 0 and board[self.row - 1][self.col - 1] is not None: #wenn gegnerische Figur ein feld diagonal ist
                if board[self.row - 1][self.col - 1].color == 0:
                    moves.append(Move(-1, -1))
            elif self.col != 7 and board[self.row - 1][self.col + 1] is not None:
                if board[self.row - 1][self.col + 1].color == 0:
                    moves.append(Move(-1, 1))

        return moves


class Turm:
    def __init__(self, startRow, startCol, color):
        self.row = startRow
        self.col = startCol
        self.color = color

    def possibleMoves(self, board):

        moves = []

        for i in range(self.row - 1, -1, -1):

            if board[i][self.col] is None or board[i][self.col].color != self.color:
                moves.append(Move(i - self.row, 0))
                if board[i][self.col] is not None and board[i][self.col].color != self.color:
                    break
            else:
                break

        for i in range(self.row + 1, 8):
            if board[i][self.col] is None or board[i][self.col].color != self.color:
                moves.append(Move(i - self.row, 0))
                if board[i][self.col] is not None and board[i][self.col].color != self.color:
                    break
            else:
                break

        for i in range(self.col - 1,  - 1, -1):
            if board[self.row][i] is None or board[self.row][i].color != self.color:
                moves.append(Move(0, i - self.col))
                if board[self.row][i] is not None and board[self.row][i].color != self.color:
                    break
            else:
                break

        for i in range(self.col + 1, 8):
            if board[self.row][i] is None or board[self.row][i].color != self.color:
                moves.append(Move(0, i - self.col))
                if board[self.row][i] is not None and board[self.row][i].color != self.color:
                    break
            else:
                break


        return moves

class Springer:
    def __init__(self, startRow, startCol, color):
        self.row = startRow
        self.col = startCol
        self.color = color

    def possibleMoves(self, board):

        moves = []

        if self.row < 6:
            if self.col != 0:
                if board[self.row + 2][self.col - 1] is None or board[self.row + 2][self.col - 1].color != self.color:
                    moves.append(Move(2, -1))
            if self.col != 7:
                if board[self.row + 2][self.col + 1] is None or board[self.row + 2][self.col + 1].color != self.color:
                    moves.append(Move(2, 1))
        if self.row != 7:
            if self.col > 1:
                if board[self.row + 1][self.col - 2] is None or board[self.row + 1][self.col - 2].color != self.color:
                    moves.append(Move(1, -2))
            if self.col < 6:
                if board[self.row + 1][self.col + 2] is None or board[self.row + 1][self.col + 2].color != self.color:
                    moves.append(Move(1, 2))
        if self.row > 1:
            if self.col != 0:
                if board[self.row - 2][self.col - 1] is None or board[self.row - 2][self.col - 1].color != self.color:
                    moves.append(Move(-2, -1))
            if self.col != 7:
                if board[self.row - 2][self.col + 1] is None or board[self.row - 2][self.col + 1].color != self.color:
                    moves.append(Move(-2, 1))
        if self.row != 0:
            if self.col > 1:
                if board[self.row - 1][self.col - 2] is None or board[self.row - 1][self.col - 2].color != self.color:
                    moves.append(Move(-1, -2))
            if self.col < 6:
                if board[self.row - 1][self.col + 2] is None or board[self.row - 1][self.col + 2].color != self.color:
                    moves.append(Move(-1, 2))
        return moves

class Läufer:
    def __init__(self, startRow, startCol, color):
        self.row = startRow
        self.col = startCol
        self.color = color


    def possibleMoves(self, board):

        moves = []

        for i in range(1, self.col+1 if self.col <= 7-self.row else 8-self.row): #links unten
            if board[self.row + i][self.col - i] is None or board[self.row + i][self.col - i].color != self.color:
                moves.append(Move(i, -i))
                if board[self.row + i][self.col - i] is not None:
                    break
            else:
                break

        for i in range(1, self.col+1 if self.col <= self.row else self.row+1): #links oben
            print(i)
            if board[self.row - i][self.col - i] is None or board[self.row - i][self.col - i].color != self.color:
                moves.append(Move(-i, -i))
                if board[self.row - i][self.col - i] is not None:
                    break
            else:
                break

        for i in range(1, 8 - self.col if 7- self.col <= 7-self.row else 8-self.row): #rechts unten
            if board[self.row+i][self.col+i] is None or board[self.row+i][self.col+i].color != self.color:
                moves.append(Move(i, i))
                if board[self.row+i][self.col+i] is not None:
                    break
            else:
                break

        for i in range(1, 8 - self.col if 7- self.col <= self.row else self.row+1): #rechts oben
            if board[self.row-i][self.col+i] is None or board[self.row-i][self.col+i].color != self.color:
                moves.append(Move(-i, i))
                if board[self.row-i][self.col+i] is not None:
                    break
            else:
                break

        return moves


class Dame:
    def __init__(self, startRow, startCol, color):
        self.row = startRow
        self.col = startCol
        self.color = color

    def possibleMoves(self, board):

        moves = []

        for i in range(self.row - 1, -1, -1):

            if board[i][self.col] is None or board[i][self.col].color != self.color:
                moves.append(Move(i - self.row, 0))
                if board[i][self.col] is not None and board[i][self.col].color != self.color:
                    break
            else:
                break

        for i in range(self.row + 1, 8):
            if board[i][self.col] is None or board[i][self.col].color != self.color:
                moves.append(Move(i - self.row, 0))
                if board[i][self.col] is not None and board[i][self.col].color != self.color:
                    break
            else:
                break

        for i in range(self.col - 1,  - 1, -1):
            if board[self.row][i] is None or board[self.row][i].color != self.color:
                moves.append(Move(0, i - self.col))
                if board[self.row][i] is not None and board[self.row][i].color != self.color:
                    break
            else:
                break

        for i in range(self.col + 1, 8):
            if board[self.row][i] is None or board[self.row][i].color != self.color:
                moves.append(Move(0, i - self.col))
                if board[self.row][i] is not None and board[self.row][i].color != self.color:
                    break
            else:
                break



        for i in range(1, self.col+1 if self.col <= 7-self.row else 8-self.row): #links unten
            if board[self.row + i][self.col - i] is None or board[self.row + i][self.col - i].color != self.color:
                moves.append(Move(i, -i))
                if board[self.row + i][self.col - i] is not None:
                    break
            else:
                break

        for i in range(1, self.col+1 if self.col <= self.row else self.row+1): #links oben
            print(i)
            if board[self.row - i][self.col - i] is None or board[self.row - i][self.col - i].color != self.color:
                moves.append(Move(-i, -i))
                if board[self.row - i][self.col - i] is not None:
                    break
            else:
                break

        for i in range(1, 8 - self.col if 7- self.col <= 7-self.row else 8-self.row): #rechts unten
            if board[self.row+i][self.col+i] is None or board[self.row+i][self.col+i].color != self.color:
                moves.append(Move(i, i))
                if board[self.row+i][self.col+i] is not None:
                    break
            else:
                break

        for i in range(1, 8 - self.col if 7- self.col <= self.row else self.row+1): #rechts oben
            if board[self.row-i][self.col+i] is None or board[self.row-i][self.col+i].color != self.color:
                moves.append(Move(-i, i))
                if board[self.row-i][self.col+i] is not None:
                    break
            else:
                break



        return moves

class König:
    def __init__(self, startRow, startCol, color):
        self.row = startRow
        self.col = startCol
        self.color = color

    def possibleMoves(self, board):

        moves = []
        if self.row != 7:
            if board[self.row + 1][self.col] is None or board[self.row + 1][self.col].color != self.color:
                moves.append(Move(1, 0))
        if self.row != 0:
            if board[self.row - 1][self.col] is None or board[self.row - 1][self.col].color != self.color:
                moves.append(Move(-1, 0))
        if self.col != 0:
            if board[self.row][self.col - 1] is None or board[self.row][self.col - 1].color != self.color:
                moves.append(Move(0, -1))
        if self.col != 7:
            if board[self.row][self.col + 1] is None or board[self.row][self.col + 1].color != self.color:
                moves.append(Move(0, 1))
        if self.row != 7 and self.col != 7:
            if board[self.row + 1][self.col + 1] is None or board[self.row + 1][self.col + 1].color != self.color:
                moves.append(Move(1, 1))
        if self.row != 7 and self.col != 0:
            if board[self.row + 1][self.col - 1] is None or board[self.row + 1][self.col - 1].color != self.color:
                moves.append(Move(1, -1))
        if self.row != 0 and self.col != 7:
            if board[self.row - 1][self.col + 1] is None or board[self.row - 1][self.col + 1].color != self.color:
                moves.append(Move(-1, 1))
        if self.row != 0 and self.col != 0:
            if board[self.row - 1][self.col - 1] is None or board[self.row - 1][self.col - 1].color != self.color:
                moves.append(Move(-1, -1))


        return moves

class Chess:
    def __init__(self, user):
        try:
            self.game = ChessGame.objects.get(host=user)
        except ObjectDoesNotExist:
            self.game = ChessGame.objects.get(player2=user)

        boardString = self.game.board
        boardList = list(boardString)
        self.board2d = [[], [], [], [], [], [], [], []]
        listCounter = 0
        for i in range(8):
            for j in range(8):
                self.board2d[i].append(boardList[listCounter])
                listCounter = listCounter + 1

        self.boardObjects = [[], [], [], [], [], [], [], []]

        for i in range(8):
            self.boardObjects[i] = [None, None, None, None, None, None, None, None]


        #Erzeugt board aus figur objekten
        for row in range(8):
            #print(len(self.boardObjects[row]))
            for col in range(8):
                c = self.board2d[row][col]

                if c == ' ':
                    self.boardObjects[row][col] = None
                else:
                    if c == 'b':
                        self.boardObjects[row][col] = Bauer(row, col, 0)

                    elif c == 'B':
                        self.boardObjects[row][col] = Bauer(row, col, 1)
                    elif c == 't':
                        self.boardObjects[row][col] = Turm(row, col, 0)
                    elif c == 'T':
                        self.boardObjects[row][col] = Turm(row, col, 1)
                    elif c == 's':
                        self.boardObjects[row][col] = Springer(row, col, 0)
                    elif c == 'S':
                        self.boardObjects[row][col] = Springer(row, col, 1)
                    elif c == 'l':
                        self.boardObjects[row][col] = Läufer(row, col, 0)
                    elif c == 'L':
                        self.boardObjects[row][col] = Läufer(row, col, 1)
                    elif c == 'd':
                        self.boardObjects[row][col] = Dame(row, col, 0)
                    elif c == 'D':
                        self.boardObjects[row][col] = Dame(row, col, 1)
                    elif c == 'k':
                        self.boardObjects[row][col] = König(row, col, 0)
                    elif c == 'K':
                        self.boardObjects[row][col] = König(row, col, 1)

    def move(self, row, col , moveRow, moveCol):
        playerField = self.board2d[row][col]
        self.board2d[moveRow][moveCol] = self.board2d[row][col]
        print(playerField)
        self.board2d[row][col] = ' '
        boardStr = ''
        for i in self.board2d:
            for j in i:
                boardStr = boardStr + j

        self.game.board = boardStr
        self.game.moveCounter = self.game.moveCounter + 1
        self.game.save()












