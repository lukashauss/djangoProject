from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChessGame
from . import chess

# Create your views here.
@login_required
def home(request):
    user = request.user
    chessGame = chess.Chess(user)

    board2d = chessGame.board2d
    for row in board2d:
        for col in row:
            print(col, end=' ')
        print('')
    return render(request, 'chess/home.html', {'board2d':board2d})

@login_required
def selectField(request):
    user = request.user
    game = chess.Chess(user)
    board = game.boardObjects

    row = int(request.GET['row'])
    col = int(request.GET['col'])
    type = request.GET['type'].strip()

    possibleMoves = board[row][col].possibleMoves(board)
    movesString = ''
    for move in possibleMoves:
        moveRow = row + move.rows
        moveCol = col + move.cols
        movesString = movesString + str(moveRow) + '|' + str(moveCol) if move is possibleMoves[-1] else movesString + str(moveRow) + '|' + str(moveCol) + ','
    print(str(possibleMoves))
    print(movesString)

    return HttpResponse(movesString)

@login_required
def move(request):
    user = request.user
    game = chess.Chess(user)


    row = int(request.GET['row1'])
    col = int(request.GET['col1'])

    moveRow = int(request.GET['row2'])
    moveCol = int(request.GET['col2'])

    game.move(row, col, moveRow, moveCol)

    board2d = game.board2d

    return render(request, 'chess/ajaxBoard.xml', {'board2d':board2d}, content_type='text/xml')

def returnMoveable(request):
    game = chess.Chess(request.user)
    moveable = True if game.game.host == request.user and game.game.moveCounter % 2 == 0 or game.game.player2 == request.user and game.game.moveCounter % 2 != 0 else False

    return HttpResponse(moveable)

def returnBoard(request):
    game = chess.Chess(request.user)
    board = game.game.board

    return HttpResponse(board)

