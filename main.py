from Create import create
from Guess import fill
print "Hello"


#matrix = create()
matrix = [[1,4,2,0,9,0,0,0,5],[7,0,0,4,0,0,0,8,9],[8,0,5,0,0,0,0,2,4],[2,0,0,0,0,4,8,0,0],[0,3,0,0,0,1,2,6,0],[0,8,0,0,7,2,9,4,1],[0,5,0,2,0,6,0,0,0],[0,2,8,0,0,9,4,1,0],[0,7,9,1,0,8,5,3,0]]

more = True 
while more:
    if fill(matrix,9,9):
        pass
    else:
        more = False 
print "Final Answer: "
for row in matrix:
    print row
