#v6.4.1 - Newer printing function (I learned how to use the format function (I didn't even know it existed! it's so convinient!))
#The first timer only starts after the matrix is created. - done X
#don't give the full long message every time entering another line.
from Create import create
from Guess import fill
from Guess import does_num
from Create import Print 
import time
print "Hello"


matrix = create()

#matrix = [[],[],[],[],[],[],[],[],[]]
#Here you may enter your own matrix, in each list enter the 9 numbers with a Comma seperating them 

#matrix = [[0,3,9,0,8,0,1,7,0],[8,0,0,0,0,0,6,0,0],[2,4,0,6,7,0,0,0,0],[0,0,0,9,0,0,7,0,3],[0,0,0,0,2,0,0,0,0],[4,0,8,0,0,5,0,0,0],[0,0,0,0,5,1,0,8,6],[0,0,6,0,0,0,0,0,7],[0,9,5,0,6,0,4,3,0],]
#sample hard matrix

#matrix = [[6,0,0,0,0,0,0,4,0],[0,1,7,4,0,0,0,0,3],[0,4,0,0,0,0,1,0,0],[2,5,6,0,0,9,0,0,0],[0,0,0,1,0,5,0,0,0],[0,0,0,3,0,0,8,5,6],[0,0,4,0,0,0,0,8,0],[3,0,0,0,0,2,5,9,0],[0,6,0,0,0,0,0,0,7,]]
#sample evil matrix (very hard one, for professional Sudoku players)

start = time.time()

Print(matrix)

fill(matrix,9,9,0)

end = time.time()
print "Length of total process: " + str(end-start) + " seconds." 





#Here the program checks itself to see if there were any changes
