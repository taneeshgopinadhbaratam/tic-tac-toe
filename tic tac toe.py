import random

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("X always goes first!")

human = input("Choose X or O: ").strip().upper()

while human != "X" and human != "O":
    human = input("Choose only X or O: ").strip().upper()

if human == "X":
    computer = "O"
else:
    computer = "X"

player = "X"

while True:

    print()

    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

    print()

    if player == human:

        print("Your turn")

        pos = input("Enter position (1-9): ")

        if pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid position")
            continue

        pos = int(pos) - 1

        if board[pos] == "X" or board[pos] == "O":
            print("Position already taken")
            continue

    else:

        print("Computer's turn")

        pos = random.randint(0, 8)

        while board[pos] == "X" or board[pos] == "O":
            pos = random.randint(0, 8)

        print("Computer chose position", pos + 1)

    board[pos] = player

    if ((board[0] == board[1] == board[2]) or
        (board[3] == board[4] == board[5]) or
        (board[6] == board[7] == board[8]) or
        (board[0] == board[3] == board[6]) or
        (board[1] == board[4] == board[7]) or
        (board[2] == board[5] == board[8]) or
        (board[0] == board[4] == board[8]) or
        (board[2] == board[4] == board[6])):

        if player == human:
            print("You win!")
        else:
            print("Computer wins!")

        break

    if all(x == "X" or x == "O" for x in board):
        print("Match draw")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"

print()

print(board[0], "|", board[1], "|", board[2])
print("--+---+--")
print(board[3], "|", board[4], "|", board[5])
print("--+---+--")
print(board[6], "|", board[7], "|", board[8])
