from Check import check_r
from Check import check_c
from Check import check_b
def fill(matrix,size_v,size_h,times):
    times += 1
    print "\nRound " + str(times)
    bspace = by_space(matrix, size_v, size_h)
    brow =  by_row(matrix, size_v,size_h)
    bcolumn = by_column(matrix,size_v,size_h)
    bbox = by_box(matrix,size_v,size_h)
    
    if bspace or brow or bcolumn or bbox: #as long as there has been a change
            for i in matrix:
                print i
            fill(matrix,size_v,size_h,times) 
    else:
        pass
    

#matrix = [[6,5,9,0,1,0,2,8,0],[1,0,0,0,5,0,0,3,0],[2,0,0,8,0,0,0,1,0],[0,0,0,1,3,5,0,7,0],[8,0,0,9,0,0,0,0,2],[0,0,3,0,7,8,6,4,0],[3,0,2,0,0,9,0,0,4],[0,0,0,0,0,1,8,0,0],[0,0,8,7,6,0,0,0,0]]


def by_row(matrix, size_v, size_h):
    changed = False 
    for row_n in range(size_v): #per row
        
        for i in range(1,10): # we run every nubmer though the nubmer i
            ans = 0 #the number if spaces which can take the number i
            res = 0 #the nubmer space which can take the number i
            for item_space in range(size_h): #
                if matrix[row_n][item_space] == 0 and does_num(matrix,row_n, item_space, i): #if the space == 0 and can hold the number i
                    ans += 1
                    res = item_space
                else:
                    pass
            if ans == 1:
                matrix[row_n][res] = i
                changed = True 
            else:
                pass      
    return changed 

def by_box(matrix,size_v, size_h):
    changed = False 
    for box_row in range(size_h/3):
        for box_column in range(size_v/3):
            for i in range(1,10):
                ans = 0 
                res_row = 0  #Every time we mark a number as 'item' it's a susptected number to be able to hold the nubmer we want to place
                res_col = 0
                for item_row in range(box_row*3, box_row*3 +3):
                    
                    for item_col in range(box_column * 3, box_column * 3 + 3): 
                        if matrix[item_row][item_col] == 0 and does_num(matrix, item_row, item_col, i):
                            ans += 1 
                            res_row = item_row
                            res_col = item_col  
                        pass
                if ans == 1:
                    matrix[res_row][res_col] = i
                    changed = True 
                 
                else:
                    pass 
    return changed  
    
            


def by_column(matrix, size_v, size_h):
    changed = False 
    for column_n in range(size_h):
        for i in range(1,10):
            ans = 0
            res = 0
            for item_row in range(size_v): #for every item in the column
                if matrix[item_row][column_n] == 0 and does_num(matrix,item_row, column_n, i):
                    ans += 1
                    res = item_row #we mark on which row (of the column) we found a result 
                else:
                    pass
            if ans == 1:
                matrix[res][column_n] = i
                changed = True 
                
            else:
                pass
    return changed 





def by_space(matrix,size_v,size_h):
    changed = False #this marks if there have been any changes so far, and so far there have been no changes

    for row_n in range(size_v): #per row

        for space_n in range(size_h): #per space in row 

            if matrix[row_n][space_n] == 0: #if the piece [in x row][in x space] == 0, if the piece we are at needs to be filled in  

                ges = guess(matrix,row_n,space_n) #ges = what guess() returned to us
                if ges != 0: # if we got an answer

                    matrix[row_n][space_n] = ges # the piece (within the matrix)= the answer
                    
                    changed = True # there had been a change
                else:
                    pass
            else:
                pass #in a case in which the space we are looking at is already full
    return changed
def does_num(matrix, row, space, num):
    if check_r(matrix, row, num) and check_c(matrix, space, num) and check_b(matrix, row, space, num):        
        return True
    else:
        return False
def guess(matrix,row,space): #checks if a number fits in 
    ans = 0 #how many answers we found
    result = 0 #what the result is
    for num in range(1,10): # we run through any possible number
        if check_r(matrix,row,num) and check_c(matrix,space,num) and check_b(matrix,row,space,num): #if the number fits in the row the column and the box
            ans += 1 #the number of result we got is up by one
            result = num
        else:
            pass
    
    if ans == 1: #in which result is the answer
        return result  
    else:
        return 0
    print "\n"
