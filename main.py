
from time import sleep
import copy

def Create_Grid(): #function that creates the grid
  Grid = []
  
  for i in range(10): #10 rows
    row = [] #row major
    
    for j in range(10):
      element = 0
      row.append(element) #append 10 zeroes, representing dead cells, to each row
      
    Grid.append(row) #finally, append the row to Grid
      
  return Grid #return Grid 
  



def Load_Design(file1, file2, Grid): #function that loads the design
  
  myFile_1 = open(file1, "r")
  Coord_1 = myFile_1.read().strip().split()
  myFile_1.close()
  
  
  myFile_2 = open(file2, "r")
  Coord_2 = myFile_2.read().strip().split()
  myFile_2.close()
  
  
  Official = [Coord_1, Coord_2]
  
  
  for a in range(0, len(Official)):
    element = Official[a]
    
    for i in range(0, len(element), 2):
      Row = int(element[i])
      Col = int(element[i+1])
      
      Grid[Row][Col] = a+1
    



def Print_Grid(Grid):
  Empty = "  " #the empty string where the grid's shape will actually form
  PlayerO = 0 #number of player O values
  PlayerX = 0 #number of player X values
  
  for i in range(10): #fills the first row with 0-9 for the columns
    Empty += f"{i} "
  
  Empty += "\n"
  
  for j in range(len(Grid)): #number of rows
    Empty += f"{j} " #each row, after the top, will start off with numbers 0 to 9, as shown in the instructions
    
    for k in range(len(Grid[0])): #number of columns
      if Grid[j][k] == 0: #if element is false, add a dash
        Empty += "- "
      
      elif Grid[j][k] == 1: #if element is 1, then add a O for Player O
        Empty += "O "
        PlayerO += 1 #add 1 to PlayerO as well
        
      elif Grid[j][k] == 2: #if element is 2, then add a X for Player X
        Empty += "X "
        PlayerX += 1 #add 1 to PlayerX as well
        
    Empty += "\n" #add a \n for each row
        
  List = [Empty, PlayerO, PlayerX] #make a list with empty, PlayerO, PlayerX
  return List #then, return the list
    




def Check_Neighbors(Row, Col, Grid):
  number = 0 #number of neighbors
  List = [] #final returning list
  
  if Row >= 1: #only if row is greater than or equal to 1, can you check top
    if Grid[Row-1][Col] != 0: #top cell
      number += 1
      List.append(Grid[Row-1][Col]) #append this value to the list as well
      
      
    if Col < len(Grid[0])-1: #only if col is less than the last (which is len(Grid[0]) -1, can you check right  
      if Grid[Row-1][Col+1] != 0: #top right cell
        number += 1
        List.append(Grid[Row-1][Col+1]) #append this value to the list as well
      
      
    if Col >= 1: #only if col is greater than 1, can you check left 
      if Grid[Row-1][Col-1] != 0: #top left cell
        number += 1 
        List.append(Grid[Row-1][Col-1]) #append this value to the list as well
      
     
  if Col >= 1: #only if col is >= 1, can you check left
    if Grid[Row][Col-1] != 0: #middle left cell
      number += 1
      List.append(Grid[Row][Col-1]) #append this value to the list as well
  
  
  if Col < len(Grid[0])-1: #only if col is less than the last, can you check right
    if Grid[Row][Col+1] != 0: #middle right cell
      number += 1 
      List.append(Grid[Row][Col+1]) #append this value to the list as well
  
  
  if Row < len(Grid)-1: #only if row is less than the last, can you check bottom
    if Grid[Row+1][Col] != 0: #bottom middle cell
      number += 1 
      List.append(Grid[Row+1][Col]) #append this value to the list as well
      
      
    if Col >= 1: #only if col is >= 1, can you check left
      if Grid[Row+1][Col-1] != 0: #bottom left cell
        number += 1
        List.append(Grid[Row+1][Col-1]) #append this value to the list as well
  
  
    if Col < len(Grid[0])-1: #only if col is less than the last, can you check right
      if Grid[Row+1][Col+1] != 0: #bottom right cell
        number += 1 
        List.append(Grid[Row+1][Col+1]) #append this value to the list as well
    
  List.append(number) #finally, append number
  
  return List #return the list




def Advance_Cell(Row, Col, Grid):
  
  call = Check_Neighbors(Row, Col, Grid) #first, call check_neighbors
  neighbors = call[len(call)-1] #the last element in the returning list, which is the number of neighbors the cell has
  
  
  if Grid[Row][Col] == 1 or Grid[Row][Col] == 2: #if the middle cell is a living cell
    if neighbors <= 1: #underpopulation, it dies
      return 0
  
    elif neighbors == 2 or neighbors == 3: #maintains, it lives
      return Grid[Row][Col] 
    
    elif neighbors >= 4: #overpopulation, it dies
      return 0 
      
      
  elif Grid[Row][Col] == 0: #if the middle cell is dead
    if neighbors == 3: #repopulation, it comes back to life - most complicated
      frequency = {} #new dictionary called frequency
      
      for i in range(0, len(call)-1): #every single element except neighbors
        num = call[i] #set call[i] equal to a variable num
        
        if num not in frequency: #if it's not in the dictionary:
          frequency[num] = 1 #make a new key-value pair with value as 1
  
        else: #if it is in the dictionary:
          frequency[num] += 1 #just add 1 to the value
          
          
      if 1 in call and 2 in call: #if both 1's and 2's are in call:
        if frequency[1] > frequency[2]: #check if 1 has a higher frequency than 2
          return 1 #if so, return 1
          
        else: 
          return 2 #if it's the opposite, then return 2
          
      else: #if only 1's or only 2's are in call:
        if 1 in call:
          return 1 #return 1 if it's only 1's
          
        else:
          return 2 #return 2's if it's only 2's
      
      
    else: #otherwise, it remains dead
      return 0 
   
   

def Advance_Grid(Grid): #function to advance the whole grid
  current = copy.deepcopy(Grid) #current grid - made a copy
  
  for i in range(len(Grid)): #for the 30 rows
    for j in range(len(Grid[0])): #60 columns
      Row = i #set the row equal to the current i value
      Col = j #set the column equal to the current j value
      
      Grid[Row][Col] = Advance_Cell(Row, Col, current) #we use current because current is the old grid that is not being updated
      
      
  return Grid #then, return the grid





def Play(): #function that runs the game
  sleep(1)
  Game = [] #official Grid for the game
  Game = Create_Grid() #call Create_Grid on Game
  Load_Design("player1.in", "player2.in", Game) #load player1 and player2
  
  Display = Print_Grid(Game) #call Print_Grid, and store it into Display
  print(f"\n\n{Display[0]}") #index 0, aka just the shape of the grid
      
  
  input("Above is the starting grid. Press any key to start the game: ")
  sleep(1)
  
  
  turns = 0 #variable to keep track of turns
  
  while True:
    Advance_Grid(Game) #call Advance_Grid on Game
    
    Display = Print_Grid(Game) #call Print_Grid, and store it into Display
    print(f"\n\n\n{Display[0]}") #index 0, aka just shape of the grid
    
    print(f"Player O has {Display[1]} cells alive.") #index 1, player O's cells
    print(f"Player X has {Display[2]} cells alive.") #index 2, player X's cells
    
    sleep(2)
    
    if Display[1] == 0: #if player O has no cells, then Player X wins
      print(f"Player X has won the game!")
      break
      
    elif Display[2] == 0: #if player X has no cells, then Player O wins
      print(f"Player O has won the game!")
      break
    
    
    if turns % 2 == 0: #every other turn is player O's turn, aka mod 2 == 0
      print(f"It's Player O's turn.")
    
    else: #all the other times, when mod 2 is 1, it's player X's turn
      print(f"It's Player X's turn.")
      
      
    Row_Add = int(input("\nEnter the row of the cell you wish to ADD: ")) #add row
    Col_Add = int(input("Enter the column of the cell you wish to ADD: ")) #add col
      
    sleep(1)
    Row_Remove = int(input("\nEnter the row of the cell you wish to KILL: ")) #remove
    Col_Remove = int(input("Enter the column of the cell you wish to KILL: "))
      
      
    if turns % 2 == 0: #if it's Player O's turn, add a 1
      Game[Row_Add][Col_Add] = 1 
      
    else: #if it's Player X's turn, add a 2
      Game[Row_Add][Col_Add] = 2 
      
      
    Game[Row_Remove][Col_Remove] = 0 #regardless of whether it is player O or player X's turn, kill the cell that they positioned with row_remove and col_remove
    
    
    turns += 1 #add 1 to turns  
    sleep(2) #sleep
    
  PlayAgain()
    
    
    
def PlayAgain():
  sleep(2)
  choice = input("\n\nWould you like to play again? Y/N ")
  
  if choice == "Y":
    sleep(1)
    Play()
    
  else:
    sleep(1)
    print("\nThank you for playing!")
    exit(1)
    


#----------------------------------------------------------------------

print("Welcome to Conway's 2-Player Game of Life! We start with a 10 by 10 grid of cells, either alive or dead.")
print("\n\nHere are the rules: Each player starts with a square. Each turn, they get to pick a position to grow a cell and pick a position to kill an opponent cell.")
print("\n\nEach generation passes by following these conditions:\n1) Any live cell with fewer than two live neighbors dies, by underpopulation")
print("\n2) Any live cell with two or three live neighbors lives on to the next generation")
print("\n3) Any live cell with more than three live neighbors dies, by overpopulation")
print("\n4) Any dead cell with exactly three live neighbors becomes alive, by reproduction")
  
sleep(2)
choice = input("\nPress any key to continue: ")

sleep(1)
Play()



    
    
    
