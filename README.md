# Sorting Algorithm Visulization
This program allows used to visulize various sorting algorithms including merge sort, insertion sort and selection sort.
# Motivation.
I was deeply intrigued by the various videos on Algorithm visulization on Youtube when I learned the sorting algorithm, as they provides an intuitive way to understand those rather complex algorithms. \
Therefore, out of interest, and to improve my skills on Python, especially for graphics, I decide to write the sorting algorithm visulizations.
# Tools.
The program was built mainly using  **pygame** library.\
Other than the library, it used various features of OOP, the classes and instances in specific.\
The usage of classes and instances make the code more readable, as it provides an neat way to represent various information for certain button and shapes.
# Compilation.
Compile the 
# Game Rule
You can skip this part if you are already familiar with the game.\
Reversi is a strategy board game\
On this game, you can either play `front-side` or `reverse-side`, denoted by `O` (front) and `X`(reverse), and the first player will play reverse-side.\
All the placement of the piece is controled by typing the coordinates.\
You can play in a position if, in any direction, you can trap more than one's opponent's piece with your existing pieces.\
All the valid move for specific colour is denoted by `*` character.\
To illustrate this using an exmaple:
```
     a     b     c     d     e     f     g     h
   _____ _____ _____ _____ _____ _____ _____ _____
  |     |     |     |     |     |     |     |     |
a |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
b |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
c |     |     |     |  *  |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
d |     |     |  *  |  O  |  X  |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
e |     |     |     |  X  |  O  |  *  |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
f |     |     |     |     |  *  |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
g |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
h |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
```
  For reverse side, the location "DC" is a valid move, because between DC and DE, there is at least one piece, in a row, are all reverse side\
  All the reverse side that's in between has to be consecutive reverse side.\
  For each move, after the piece is placed, all the opposite piece (for example, if it is front's move, then the opposite means reverse side) that's between the same    colour (in which case, front) will be flipped and change to opposite side.\
  If reverse side placed piece on dc, then the board will become
```
     a     b     c     d     e     f     g     h
   _____ _____ _____ _____ _____ _____ _____ _____
  |     |     |     |     |     |     |     |     |
a |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
b |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
c |     |     |  *  |     |  *  |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
d |     |     |  X  |  X  |  X  |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
e |     |     |  *  |  X  |  O  |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
f |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
g |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
  |     |     |     |     |     |     |     |     |
h |     |     |     |     |     |     |     |     |
  |_____|_____|_____|_____|_____|_____|_____|_____|
```
Noted that since the front side piece on cd is between two reverse side, then it is flipped.
# End of the game:
If only one of player cannot make any move, the game will switch side instantly\
After the point where no move can be made for both player, the game terminates.\
The player with more pieces on the board win.\
Enjoy.

