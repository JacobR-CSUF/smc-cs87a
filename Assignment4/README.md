### Program  

You will use loops to write a simple game, in which there is a 5x11 grid with a Player and a Destination. The grid is made of text, where every character is an "x" if it is empty, "@" if it is the Player, and "G" if it is the Destination.  

The starting game state is shown below:  
<img width="106" height="136" alt="image" src="https://github.com/user-attachments/assets/4331dd83-c243-432b-a585-9a0de41ab15c" />  

The user is prompted to enter a movement command:  

* `w` moves the Player up
* `a` moves the Player to the left
* `s` moves the Player down
* `d` moves the Player to the right

The border of the game is not considered part of the grid, and is instead just a wall. The Player cannot move into the walls, and if the user attempts to do so, the move is considered valid but the Player will not move. 

This behavior is shown below:  
<img width="106" height="275" alt="image" src="https://github.com/user-attachments/assets/1c665941-b977-4263-b9f0-3e55fc4efc67" />  

The game continues until the Player moves into the Destination, at which point the game displays Victory! to the terminal, and the game ends (therefore, there is no more looping).  

This is shown below:  
<img width="101" height="149" alt="image" src="https://github.com/user-attachments/assets/98add92a-dded-46c9-94a2-087e17271603" />

