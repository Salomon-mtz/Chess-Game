#proyect.py
#Team 1: Elí Martínez- A01653876
#Diego Figueroa- A01655047
#Capstone project: Chess board
#This program creates a chess board with 3 pieces, the white queen and king, and the black king. It prints the posible movements of the black king and prints the if the black king is on check and checkmate. 

# import random to use it in the function of setting the pieces in the board.
import random 

# changeStamp helps us to change the at symbol into the hashtag.
# It Receives s that it is an equal character patter.
# It returns an interspersed order of characters. 
def changeStamp(s):
    if s == "@":
        s = "#"
    else:
        s = "@"
    return s

# makeBoard creates the board with an 8x8 matrix with the stamps @ and #. In other words, this function creates a 2D array of characters as the board and returns it.
# It receives nothing to be able to run.
# The function returns us the board made of interleaved string characters.
def makeBoard():
    board = []
    stamp = "@"
    for r in range (8):
        row = []
        for c in range (8):
            row.append(stamp)
            stamp = changeStamp(stamp) 
        board.append(row)
        stamp = changeStamp(stamp)
    return board

# printBoard receives the 2D array of characters as the board and prints it in a vertical form like a traditional chess game.  
# It receives the board created in makeBoard function.
# Returns the board as a chessboard without commas and brackets. 
def printBoard (board):
    for r in range (8):
        for c in range (8):
            print(board[r][c], end= " ")
        print()

# setBoard sets the white king and queen and the black king on the board randomly, but without placing two pieces in the same place.
# It receives the board created in makeBoard function.
# It returns the board with the White Queen, White King, and Black King placed randomly, but without placing two pieces in the same place.
def setBoard (board):
  #White king: K
    rowK = random.randrange (0,8)
    colK = random.randrange (0,8)
    board [rowK][colK] = "K"
  #Black king: k
    rowk = random.randrange (0,8)
    colk = random.randrange (0,8)
    diffR = abs(rowK-rowk)
    diffC = abs(colK-colk)
    while diffR < 2 and diffC < 2:
            rowk = random.randrange (0,8)
            colk = random.randrange (0,8)
            diffR = abs(rowK-rowk)
            diffC = abs(colK-colk)
    board [rowk][colk] = "k"
  #White Queen: Q
    rowQ = random.randrange (0,8)
    colQ = random.randrange (0,8)
    while board[rowQ][colQ] == "K" or board[rowQ][colQ] == "k":
            rowQ = random.randrange (0,8)
            colQ = random.randrange (0,8)
    board [rowQ][colQ] = "Q"
    
    return board
    
# findPiece gives us the coordinates where the piece that we put as a parameter is positioned.
# It receives the board created in makeBoard function and the character of the specific piece what you want to locate.
# Returns the coordinates of the character we are looking for. 
def findPiece(board, piece):
  for i in range (8):
    for k in range (8):
      if board[i][k] == piece:
        return [i,k]
  return None

# bounds establishes the bounds of our board so the pieces do not move away from the range of the matrix.
# It receives the coordinates of the character we are looking for given by the function of findPiece.
# Returns True or False depending on whether the movements are within the board parameter.
def bounds(position):
  if position [0] >= 0 and position [0] <= 7 and position [1] >= 0 and position [1] <= 7:
    return True
  else:
    return False

# NoOutof Bounds eliminates the possible moves where the pieces might be out of the matrix.
# It receives the coordinates of the character we are looking for given by the function of findPiece.
# Returns True or False depending on the result of bounds function, so if the positions are not in the range it returns True.
def NoOutOfBounds(positions):
  for p in positions:
    if bounds(p) == False:
      return True
  return False 

# CheckBoard creates all possible moves for the white queen, the white king, and the black king. In the same way, it eliminates from the black king's list of movements, the moves that they have in common with the other two pieces. Finally, apart from giving us the final moves of the black king, it tells us if it is check and checkmate.
# It receives the board created in makeBoard function.
# Returns us a list with the movements of the black king and if it was check and checkmate.
def CheckBoard(board):
  #Defines the position of the pieces and defines the variables of the columns and rows. 
  posQ = findPiece(board, "Q")
  K = findPiece(board, "K")
  k = findPiece(board, "k")
  rk = k[0]
  ck = k[1]
  rK= K[0]
  cK= K[1]
  
  #Creates an empty list for the positions of the queen and defines de conditions of check and checkmate.
  positionsQ = []
  check = False
  checkmate = False
  
  #Creates the list of possible movements for the black king. 
  positionk = [[rk,  ck+1],
              [rk-1, ck+1],
              [rk-1, ck],
              [rk-1, ck-1],
              [rk,   ck-1],
              [rk+1, ck-1],
              [rk+1, ck],
              [rk+1, ck+1]]
  
  #This while eliminates the positions where the black king can't move because they are out of bounds. 
  while NoOutOfBounds(positionk):
    for position in positionk:
      if bounds(position) == False:
        positionk.remove(position)


  #Creates the list of the possible movements for the white king. 
  positionsK = [[rK,  cK+1],
              [rK-1,  cK+1],
              [rK-1,  cK],
              [rK-1,  cK-1],
              [rK,    cK-1],
              [rK+1,  cK-1],
              [rK+1,  cK],
              [rK+1,  cK+1]]

  #This while eliminates the positions where the white king can't move because they are out of bounds.  
  while NoOutOfBounds(positionsK):
    for position in positionsK:
      if bounds(position) == False:
        positionsK.remove(position)
  
  #Defines the columns and rows for the queen movements.
  r = posQ [0]
  c = posQ [1]
  rq = r
  cq = c
  
  #Adds to the list postionsQ, the possible moves to the right of the queen.
  for cq in range (c+1,8):
    if "k" == board[rq][cq]:
      check = True
    if "K" == board[rq][cq]:
      break
    positionsQ.append([rq, cq])
  
  #Adds to the list postionsQ, the possible moves to the left of the queen.
  for cq in range (c-1,-1,-1):
    if "k" == board[rq][cq]:
      check = True
    if "K" == board[rq][cq]:
      break
    positionsQ.append([rq,cq])
  
  #Initialize the variable of the columns because we are not using it. 
  cq= c 
  #Adds to the list postionsQ, the possible moves of the bottom of the queen.
  for rq in range (r+1,8):
    if "k" == board[rq][cq]:
      check = True
    if "K" == board[rq][cq]:
      break
    positionsQ.append([rq, cq])
   #Adds to the list postionsQ, the possible moves of the top of the queen.
  for rq in range (r-1,-1,-1):
    if "k" == board [rq][cq]:
      check = True
    if "K" == board[rq][cq]:
      break
    positionsQ.append([rq, cq])
  
  #Defines the variables of the columns and rows and adds 1 to both because the movement is from down and right. 
  rq = r + 1
  cq = c + 1
  #Creates a cycle where if the movement of the queen matches with the position of the black king, then the condition check becomes True. And if the movement matches the position of the white king, those movements are eliminated and the while cycle breaks.
  while rq < 8 and cq < 8:
    if "k" == board[rq][cq]:
      check = True
    if "K" == board[rq][cq]:
      break
    positionsQ.append ([rq, cq])
    rq += 1
    cq += 1
  
  #Defines the variables of the columns and rows and adds 1 to columns and subtracts 1 to rows because the movement is from up and right.
  rq = r - 1
  cq = c + 1
  #Creates a cycle where if the movement of the queen matches with the position of the black king, then the condition check becomes True. And if the movement matches the position of the white king, those movements are eliminated and the while cycle breaks.
  while rq > -1 and cq < 8:
    if "k" == board[rq][cq]:
      check = True
    if "K" == board[rq][cq]:
      break
    positionsQ.append ([rq, cq])
    rq -= 1
    cq += 1
  
  #Defines the variables of the columns and rows and adds 1 to rows and subtract 1 to columns because the movement is from down and left.
  rq = r + 1 
  cq = c - 1
  #Creates a cycle where if the movement of the queen matches with the position of the black king, then the condition check becomes True. And if the movement matches the position of the white king, those movements are eliminated and the while cycle breaks.
  while rq < 8 and cq > -1:
    if "k" == board[rq][cq]:
      check = True
    if "K" == board[rq][cq]:
      break
    positionsQ.append ([rq, cq])
    rq += 1
    cq -= 1

  #Defines the variables of the columns and rows and subtracts 1 to both because the movement is from up and left. 
  rq = r - 1 
  cq = c - 1
  #Creates a cycle where if the movement of the queen matches with the position of the black king, then the condition check becomes True. And if the movement matches the position of the white king, those movements are eliminated and the while cycle breaks.
  while rq > -1 and cq > -1:
    if "k" == board[rq][cq]: 
      check = True
    if "K" == board[rq][cq]: 
      break
    positionsQ.append ([rq, cq])
    rq -= 1
    cq -= 1
  
 #This while eliminates the positions where the white queen can't move because they are out of bounds.   
  while NoOutOfBounds(positionsQ):
    for position in (positionsQ):
      if bounds(position) == False:
        positionsQ.remove(position)
        
  #This repetition structure is in charge of removing the moves of either the Queen or the white king from the black king's move list.
  counter = 0
  while counter < 4:
    for elem in positionk:
      if elem in positionsQ or elem in positionsK:
       positionk.remove(elem)
    counter = counter + 1

  #We decided to repeat the previous cycle in case it misses any option that should not be on the list.
  counter = 0
  while counter < 4:
    for elem in positionk:
      if elem in positionsQ or elem in positionsK:
       positionk.remove(elem)
    counter = counter + 1

  #Checks the list of possible movements of the black king and the condition check, where if both accomplish then the checkmate is True. 
  if len(positionk) == 0 and check == True:
    checkmate = True

  #As we can only return once in the function, we decided to return a list with all the required elements.
  return [positionk, check, checkmate, positionsQ,positionsK]


#Gives a selection input where you can enter 1 for the program to give the board or 2 for you to input the board in the program. 
b = []
choice = int(input())
if choice == 1:  
  b = makeBoard()
  b = setBoard (b)
elif choice == 2:
  for r in range (8):
    line = input() 
    line = line.strip() 
    row = line.split (" ")
    b.append(row)

#Finally, we call the printBoard and CheckBoard functions and print the black king's moves. In the same way, we print if it was check and also if it was checkmate.
printBoard(b)
movek = CheckBoard (b)
print ("Black King Moves: ", movek[0])
print ("Check: ", movek[1])
print("Checkmate: ", movek[2])

