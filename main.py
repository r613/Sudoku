from Create import create
from Guess import fill
from Guess import does_num
print "Hello"


matrix = create()
#matrix = [[0,3,9,0,8,0,1,7,0],[8,0,0,0,0,0,6,0,0],[2,4,0,6,7,0,0,0,0],[0,0,0,9,0,0,7,0,3],[0,0,0,0,2,0,0,0,0],[4,0,8,0,0,5,0,0,0],[0,0,0,0,5,1,0,8,6],[0,0,6,0,0,0,0,0,7],[0,9,5,0,6,0,4,3,0],]


for row in matrix:
    print row

fill(matrix,9,9,0)

print "\n  Final Answer: \n "

for row in matrix:
    print row



#Here the program checks itself to see if there were any changes
verified = True 
for row_n in range(9):
    for space_n in range(9):
        num  = matrix[row_n][space_n]
        matrix[row_n][space_n] = 0
        if does_num(matrix,row_n,space_n, num):
            pass
        else:
            verified = False 
        matrix[row_n][space_n] = num 
print verified 
