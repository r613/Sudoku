v1.0
from Create import create
from Create import Print
import time
#from Guess import by_space
#from Guess import by_column
#from Guess import by_row
from Guess import by_box

def search(matrix):
    for row in range(9):
        for column in range(9):
            if matrix[row][column] == 0:
                for i in range(1,10):
                    if fits(matrix,row,column,i):
                        temp_matrix = [x[:]for x in matrix]
                        temp_matrix[row][column] = i
                        res = search(temp_matrix)
                        if res:
                            return res
                return False
    if full(matrix):
        return matrix
    else:
        return False
def fits(matrix,row_n,column_n,a):
    if fits_r(matrix,row_n,a) and fits_c(matrix,column_n,a) and fits_b(matrix,row_n,column_n,a):
        return True
    else:
        return False
def fits_r(matrix,row_n,a):
    for unit in matrix[row_n]:
        if unit == a:
            return False
    return True

def fits_c(matrix,column_n,a):
    for row in matrix:
        if row[column_n] == a:
            return False
    return True
  

def fits_b(matrix,row_n,column_n,a):
    for row_num in range( (row_n/3)*3,(row_n/3)*3+3 ):
        for col_num in range( (column_n/3)*3,(column_n/3)*3+3):
            if matrix[row_num][col_num] == a:
                return False
    return True

def full(matrix):
    for row_n in range(9):
        for column_n in range(9):
            t = matrix[row_n][column_n]
            matrix[row_n][column_n] = 0
            res = fits(matrix,row_n,column_n,t)
            matrix[row_n][column_n] = t
            if res == False:
                return False
    return True
def find(matrix):
    searching = True
    while searching:
        searching = False
        if by_space(matrix) or by_row(matrix) or by_column(matrix) or by_box(matrix):
            searching = True
        else:
            pass
    return matrix
def by_space(matrix):
    changes = False
    for row_n in range(9):
        for column_n in range(9):
            if matrix[row_n][column_n]==0:
                pos = 0#this resembles how many difference possible outcomes this space can have
                res = 0#this resembles the latest result we found for this piece
                for i in range(1,10):
                    if fits(matrix,row_n,column_n,i):
                        pos += 1
                        res = i
                if pos == 1:
                    matrix[row_n][column_n] = res
                    changes = True
    return changes
def by_row(matrix):
    changed = False
    for row_n in range(9):
        for i in range(1,10):
            pos = 0
            res = 0
            exists = False
            #for column_n in range(9): if matrix[row_n][column_n] == i: skip this part of the process
            for unit in matrix[row_n]:
                if unit == i:
                    exists = True
            if exists == False:
                for column_n in range(9):
                    if matrix[row_n][column_n] == 0 and fits(matrix,row_n,column_n,i):
                        pos += 1
                        res = column_n
                if pos == 1:
                    matrix[row_n][res] = i 
                    changed = True
    return changed
    
def by_column(matrix):
    changed = False
    for column_n in range(9):
        for i in range(9):
            pos = 0 
            res = 0
            exists = False
            for row_n in range(9):
                if matrix[row_n][column_n] == i:
                    exists = True
            if exists == False:
                for row_n in range(9):
                    if matrix[row_n][column_n] == 0 and fits(matrix,row_n,column_n,i):
                        pos += 1
                        res = row_n 
                if pos == 1:
                    matrix[res][column_n] = i
                    changed = True
    return changed

"""
def by_column(matrix):
    changed = False
    for column_n in range(9):
        for i in range(1,10):
            pos = 0
            res = 0
            exists = False
            for row_n in range(9):
                if matrix[row_n][column_n] == i:
                    exists = True
            if exists == False:
                for row_n in range(9):
                    if fits(matrix,row_n,column_n,i):
                        pos += 1
                        res = row_n 
                if pos == 1:
                    matrix[res][column_n] = i
                    changed = True
    return changed 
def by_box(matrix):
    return False
"""
matrix = [[0,3,9,0,8,0,1,7,0],[8,0,0,0,0,0,6,0,0],[2,4,0,6,7,0,0,0,0],[0,0,0,9,0,0,7,0,3],[0,0,0,0,2,0,0,0,0],[4,0,8,0,0,5,0,0,0],[0,0,0,0,5,1,0,8,6],[0,0,6,0,0,0,0,0,7],[0,9,5,0,6,0,4,3,0],]

#matrix = [[6,0,0,0,0,0,0,4,0],[0,1,7,4,0,0,0,0,3],[0,4,0,0,0,0,1,0,0],[2,5,6,0,0,9,0,0,0],[0,0,0,1,0,5,0,0,0],[0,0,0,3,0,0,8,5,6],[0,0,4,0,0,0,0,8,0],[3,0,0,0,0,2,5,9,0],[0,6,0,0,0,0,0,0,7,]]
Print(matrix)
speed = []
for i in range(100):
    start = time.time()
    temp_matrix = [x[:]for x in matrix]
    find(temp_matrix)    
    speed.append(time.time()-start)
for stuff in speed:
    print stuff      
sum = 0
for i in speed:
    sum += i

print "The average is: {}\n The Sum is: {}".format(sum / len(speed),sum)

#matrix = find(matrix)
#res = search(matrix)
#Print(res)
