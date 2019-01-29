import sys
from Check import check_r
from Check import check_c
from Check import check_b
from Create import create 
from Check import checker
from Input import Input 
import time

                    
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
        
        if checker(matrix):
            print "\n \n Solved!\n"
            for i in matrix:
                print i
        else:
            choice = Input("The script you entered seems to be a very challenging one, this might take some time, how much of the process would you like to see? Enter the nubmer you would like: \n 1. See nothing. \n 2. See how deep it is in every process - This choice may slightly slow down the process.\n 3. See the entire process - This has a large affect on the processing time.\n")
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
            for i in matrix:
                print i
            if debugger(matrix):
                print "The puzzle has been confirmed as possible!"
            else:
                "We got a problem!"
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
    for row in matrix:
        print row
    
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