"""
Each cell in a 2D grid contains either a wall ('W') or an enemy ('E'), 
or is empty ('0'). Bombs can destroy enemies, but walls are too strong to be destroyed. 
A bomb placed in an empty cell destroys all enemies in the same row and column, but the destruction stops once it hits a wall.

field = [["0", "0", "E", "0"],
         ["W", "0", "W", "E"],
         ["0", "E", "0", "W"],
         ["0", "W", "0", "E"]]

the output should be
bomber(field) = 2.

Placing a bomb at (0, 1) or at (0, 3) destroys 2 enemies.


"""

def bomber(field):