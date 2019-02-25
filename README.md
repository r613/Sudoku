# Sudoku

Python 2.7 

 - Minor bug program asks how to solve second part after being solved

Please leave feedback!
icreatemyweb@Gmail.com

The code isn't totally bug free, so please don't enter letters or any other symbol, and 9 characters per row, not more or less.

Feel free to add the matrix into the code itself (There are instuctions with exapmles inside for doing so, just don't forget to leave the #hashtag only by rows you want left out)


v6.4 - Stable (No bugs found yet, and this time I looked!)
Released!


v6.2 
Now after entering the puzzle, the user is able to change any of the lines.


v5.1 - more user friendly 
(leading towards the next update in which I really want to get much more user friendly)
The user gets to choose if to see the program in live action 
The program directs the user towards editing his matrix in the code itself 
and of course the awesomest change:
See how long it took the program to run, 
if there is a dialog in the middle, there will be another timer for the other process (the one which actually Guesses)


v5.0 

by_space(matrix) - if there are any spaces which can only hold 1 specific number 

by_row(matrix) - If there is only one space within the row which can contain the number i

by_column(matrix) - if there is only one space within the column which can contain the number i

by_box(matrix) - if there is only one space within the box (3x3) which can hold a specific number 

Guess(matrix) - this function literately just Guesses until it gets the right answer, it's recursive, 
for the first empty space it finds in the matrix, it fills it in with the first number that fits in there, Guess(matrix) and goes on, and after being rejected will move on to further number, 
 - cute bonus to Guess(), you can see how long into the recursive it is, by the stars that show up as the guessing goes on, and the stars go in and jump out, and when it reaches the max (the amount of empty spaces in the puzzle) the program will print the result
 - the function can solve any puzzle, but it takes more time, so the program first try the normal functions (under 1s), and if that fails it tries Guess(matrix) - which can take 30s-2m 

debugger(matrix) - runs through the matrix to see if there are no mistakes (no doubles in each row, column and box)

checker(matrix) - which turned out to be kinda useful for making Guess() fully functional (I added it in a further stage(until then i just left Guess() in an infinite loop so i can see the result)), the function checks if the puzzle has any pieces left to be filled.
