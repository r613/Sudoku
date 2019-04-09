#Sudoku 
import time
from User import creator
from Solver import Guess

from Solver import fits
from Solver import in_row
from Solver import in_column
from Solver import in_box 
from Solver import is_full
from Solver import checker


#matrix = [[7, 1, 0, 8, 0, 5, 4, 0, 9],[9, 0, 4, 2, 6, 7, 3, 1, 0],[0, 0, 0, 4, 0, 9, 5, 7, 6],[0, 0, 0, 0, 8, 3, 4, 7, 0],[4, 0, 0, 0, 5, 6, 9, 8, 1],[8, 7, 1, 9, 0, 2, 6, 3, 0],[1, 0, 9, 5, 7, 4, 2, 6, 3],[3, 0, 7, 2, 0, 8, 1, 4, 5],[5, 4, 2, 3, 6, 1, 8, 0, 0]] #easier
#matrix = creator()
matrix = [[0, 0, 0, 0, 0, 0, 3, 0, 0],[0, 1, 0, 0, 9, 3, 4, 0, 6],[0, 0, 9, 0, 1, 0, 0, 0, 0],[0, 0, 1, 0, 3, 9, 8, 0, 0],[2, 0, 0, 0, 4, 0, 0, 0, 0],[0, 7, 0, 2, 5, 0, 0, 0, 0],[0, 0, 0, 0, 2, 0, 0, 0, 4],[0, 0, 0, 0, 0, 0, 0, 3, 5],[7, 2, 3, 0, 0, 0, 0, 6, 0]]
#very hard matrix


start = time.time()
res = Guess(matrix)
print "The Solving time was: {}".format(time.time()-start)
for i in res:
        print i
if is_full(res) and checker(res):
        print "The Solution has been Debugged and confirmed"
else:
        print "There is a problem with the solution"
        if is_full(res):
                print "The solution is full"
        if checker(res):
                print "The Solution has no mistakes (no number repearing itself within a row/column/box)"



