from Check import check_r
from Check import check_c
from Check import check_b
def fill(matrix,size_v,size_h):
    changed = False 
    bspace = by_space(matrix, size_v, size_h)
    brow = by_row(matrix, size_v,size_h)
    if bspace or brow: #as long as there has been a change
            changed = True 
    return changed

def by_row(matrix, size_v, size_h):
    changed = False 
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
def guess(matrix,row,space):
    ans = 0 #how many answers we found
    result = 0 #what the result is
    for num in range(1,10): # we run through any possible number
        if check_r(matrix,row,num) and check_c(matrix,space,num) and check_b(matrix,row,space,num): #if the number fits in the row the column and the box
            ans += 1 #the number of result we got is up by one
            result = num
        else:
            pass
    
    print "We ran through the matrix once, here is the result:"
    for i in matrix:
        print i
    if ans == 1: #in which result is the answer
        return result  
    else:
        return 0
    print "\n"