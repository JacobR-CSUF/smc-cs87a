# CS 87A Lu -- Module 7 Assignment
# STUDENT NAME: Jacob Rodas

# GLOBAL CONSTANTS (don't touch these)
HORIZONTAL_WALL = "+-----------+"
FILLER_ROW = "|xxxxxxxxxxx|"
NUM_ROWS = 5 # NUM_ROWS only counts the rows that can be
reached by the player, the walls are not counted
NUM_COLUMNS = 11 # NUM_COLUMNS only counts the columns that can
be reached by the player, the walls are not counted
DESTINATION_X = 4
DESTINATION_Y = 4

# FUNCTION DEFINITIONS
# insert_character_in_row() returns a string that is equivalent to the FILLER_ROW constant,
# except up to two characters in the row are replaced.
def insert_character_in_row(first, second=-1, first_character='x', second_character='x'):
  row = "|"
  for i in range(0, NUM_COLUMNS):
    if i+1 == first:
      row = row + first_character
    elif i+1 == second:
      row = row + second_character
    else:
      row = row + "x"
  return row + "|"


# display() prints the full grid.
def display(player_x, player_y, destination_x=DESTINATION_X, destination_y=DESTINATION_Y):
  
  print(HORIZONTAL_WALL)
  
  for row in range(1, NUM_ROWS + 1):
    if row == player_y and row == destination_y:
      # Both player and destination on same row
      print(insert_character_in_row(player_x, destination_x, '@', 'G'))
    elif row == player_y:
      # Only player on this row
      print(insert_character_in_row(player_x, -1, '@', 'x'))
    elif row == destination_y:
      # Only destination on this row
      print(insert_character_in_row(destination_x, -1, 'G', 'x'))
    else:
      # Empty row
      print(FILLER_ROW)
      
  print(HORIZONTAL_WALL)
  
# main() must maintain information about the game (whether the Player has won, and where they are)
def main():
  # Initializing game information is done for you
  player_won = False
  player_x = 1
  player_y = 1
  
  display(player_x, player_y)
  
  while not player_won:  
    move = input("w/a/s/d: ")
    
    # Move player position on key entry:
    if move == 'w' and player_y > 1:
      player_y -= 1
    elif move == 's' and player_y < NUM_ROWS:
      player_y += 1
    elif move == 'a' and player_x > 1:
      player_x -= 1
    elif move == 'd' and player_x < NUM_COLUMNS:
      player_x += 1
    elif move not in ['w', 'a', 's', 'd']: # Invalidate if not [WASD]
      print("Invalid.")
    if player_x == DESTINATION_X and player_y == DESTINATION_Y:
      player_won = True
      print("Victory!")
    else:
      display(player_x, player_y)
      
# The main conditional is provided for you
if __name__ == "__main__":
main()
