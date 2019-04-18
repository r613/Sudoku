import sys
from Check import check_r
from Check import check_c
from Check import check_b
from Create import create 
from Check import checker
from Input import Input 
from Create import Print
import time


                    
def fill(matrix,size_v,size_h,times):
    times += 1
    print "\nRound " + str(times)
    bspace = by_space(matrix)
    brow =  by_row(matrix)
    bcolumn = by_column(matrix)
    bbox = by_box(matrix)
    
    if bspace or brow or bcolumn or bbox: #as long as there has been a change
            Print(matrix)
            fill(matrix,size_v,size_h,times) 
    else:
        
        if checker(matrix):
            print "\n \n Solved!\n"
            Print(matrix)
        else:
            choice =1# Input("The script you entered seems to be a very challenging one, this might take some time, how much of the process would you like to see? Enter the nubmer you would like: \n 1. See nothing. \n 2. See how deep it is in every process - This choice may slightly slow down the process.\n 3. See the entire process - This has a large affect on the processing time.\n")
            start = time.time()
            if choice == 1:
                matrix = Guess(matrix) #This is the really hard stuff (when it's a really hard level)
            elif choice == 2:
                
                matrix = Guess_2(matrix,0)
                print "The stars resemble how many numbers the process is trying to fill in at this point."
            elif choice == 3:
                matrix = Guess_3(matrix,0)
                print "\n\nAbove you see what matrices the program was testing."
            else:
                print "Only a 1,2 or 3."
                fill(matrix,9,9,0)
            end = time.time()
            print "Length of this process (basically just tried any possibility): " + str(end - start)
            print "Matrix in final"
            Print(matrix)
            if debugger(matrix):
                print "The puzzle has been confirmed as possible!"
            else:
                "We got a problem!"

def by_row(matrix):
    changed = False
    for row_n in range(9):
        for i in range(1,10):
            pos = 0#resembles how many spaces can hold this number 
            res = 0#the placing of the space which can contain the number (if there is more than 1 space then it doesn't matter anyways)
            exists = False#if this number already exists in this row
            for column_n in range(9):
                if matrix[row_n][column_n] == 0 and fits(matrix,row_n,column_n,i):
                    pos += 1
                    res = column_n 
            if pos == 1:
                matrix[row_n][res] = i
                changed = True
    return changed
    """
def by_row(matrix):
    changed = False 
    for row_n in range(9): #per row
        
        for i in range(1,10): # we run every nubmer though the nubmer i
            ans = 0 #the number if spaces which can take the number i
            res = 0 #the nubmer space which can take the number i
            for item_space in range(9): #
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
    return changed """

def by_box(matrix):
    changed = False 
    for box_row in range(9/3):
        for box_column in range(9/3):
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
            
def by_column(matrix):
    changed = False 
    for column_n in range(9):
        for i in range(1,10):
            ans = 0
            res = 0
            for item_row in range(9): #for every item in the column
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
"""
def by_space(matrix):
    changed = False #this marks if there have been any changes so far, and so far there have been no changes

    for row_n in range(9): #per row

        for space_n in range(9): #per space in row 

            if matrix[row_n][space_n] == 0: #if the piece [in x row][in x space] == 0, if the piece we are at needs to be filled in  

                ges = guess(matrix,row_n,space_n) #ges = what guess() returned to us
                if ges != 0: # if we got an answer

                    matrix[row_n][space_n] = ges # the piece (within the matrix)= the answer
                    
                    changed = True # there had been a change
                else:
                    pass
            else:
                pass #in a case in which the space we are looking at is already full
    return changed"""

def debugger(matrix):
  verified = True 
  for row_n in range(9):
      for space_n in range(9):
          num = matrix[row_n][space_n]
          matrix[row_n][space_n] = 0
          if does_num(matrix, row_n, space_n, num):
              pass
          else:
              verified = False 
          matrix[row_n][space_n] = num
  return verified 


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

def Guess(matrix):
    
    
    if checker(matrix):
        return matrix
    else:
        pass
    
    for row in range(9): # per row  
        for space in range(9): # per piece in row 
            if matrix[row][space] == 0: #if the space is empty 
                 
                for i in range(1,10): #i run every number 
                    if does_num(matrix, row, space, i): #if i find a number that fits 
                        
                        temp_matrix = [x[:] for x in matrix] #temp_matrix is a copy 
                        temp_matrix[row][space] = i #in the copy we put the suspected number (i) 
                        result = Guess(temp_matrix) # if the nubmer fits all the way (we check all the further combinations) if it worked out we make matrix the real matrix
                        if checker(result):
                            return result

                        else:
                            pass 

                return matrix
def Guess_2(matrix,deep):
    
    print '\n'
    print "*" * deep #we check how deep it is (how many 'layers' of recursion there are)
    if checker(matrix):
        return matrix
    else:
        pass
    
    for row in range(9): # per row  
        for space in range(9): # per piece in row 
            if matrix[row][space] == 0: #if the space is empty 
                 
                for i in range(1,10): #i run every number 
                    if does_num(matrix, row, space, i): #if i find a number that fits 
                        
                        temp_matrix = [x[:] for x in matrix] #temp_matrix is a copy 
                        temp_matrix[row][space] = i #in the copy we put the suspected number (i) 
                        result = Guess_2(temp_matrix, deep+1) # if the nubmer fits all the way (we check all the further combinations) if it worked out we make matrix the real matrix
                        if checker(result):
                            return result

                        else:
                            pass 

                return matrix
def Guess_3(matrix,deep):
    

    

    if checker(matrix):
        return matrix
    else:
        pass
    
    print '\n'
    print "*" * deep #we check how deep it is (how many 'layers' of recursion there are)
    Print(matrix)
    
    for row in range(9): # per row  
        for space in range(9): # per piece in row 
            if matrix[row][space] == 0: #if the space is empty 
                 
                for i in range(1,10): #i run every number 
                    if does_num(matrix, row, space, i): #if i find a number that fits 
                        
                        temp_matrix = [x[:] for x in matrix] #temp_matrix is a copy 
                        temp_matrix[row][space] = i #in the copy we put the suspected number (i) 
                        result = Guess_3(temp_matrix, deep+1) # if the nubmer fits all the way (we check all the further combinations) if it worked out we make matrix the real matrix
                        if checker(result):
                            return result

                        else:
                            pass 

                return matrix
def does_num(matrix, row, space, num):
    if check_r(matrix, row, num) and check_c(matrix, space, num) and check_b(matrix, row, space, num):        
        return True
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