def Guess(matrix):
        if is_full(matrix):
                if checker(matrix):
                        return matrix
                else:
                        return        
        for row_n in range(9):
                for column_n in range(9):
                        if matrix[row_n][column_n] == 0:
                                for i in range(1,10):
                                        if fits(matrix,row_n,column_n,i):
                                                temp_matrix = [row[:] for row in matrix]
                                                
                                                temp_matrix[row_n][column_n] = i
                                                
                                                res = Guess(temp_matrix)
                                                if res:
                                                        return res
                                                else:
                                                        pass
                                                """print "This is the res"
                                                print res
                                                if res:
                                                        print "Yay!"
                                                        return res
                                                else:
                                                        pass"""
                                        else:
                                                pass #The attempted number didn't fit 
                                
                                return
                                print "This should never happen" #No numbers fit in the space, this matrix is invalid - Give Up!
        print "I'm not sure how we got here but that's totally not Awesome!"
def fits(matrix,row_n,column_n,a):#a is the number wer'e attempting to fit in
        if in_row(matrix,row_n,a) and in_column(matrix,column_n,a) and in_box(matrix,row_n,column_n,a):
                return True
        else:
                return False 
def in_row(matrix,row_n,a):
        for i in range(9):
                if a == matrix[row_n][i]:
                        return False 
        return True
def in_column(matrix,column_n,a):
        for i in range(9):
                if matrix[i][column_n] == a:
                        return False 

        return True
def in_box(matrix,row_n,column_n,a):
        for row_num in range( (row_n/3) * 3, (row_n/3) * 3 + 2 ):
                for col_num in range( (column_n/3) * 3, (column_n/3) * 3 + 2 ):
                        if matrix[row_num][col_num] == a:
                                return False 
        return True
def is_full(matrix):
        for row_n in range(9):
                for column_n in range(9):
                        if matrix[row_n][column_n] == 0:
                                return False 

        return True
def checker(matrix):
        
        for row_n in range(9):
                for column_n in range(9):
                        a = matrix[row_n][column_n]
                        matrix[row_n][column_n] = 0
                        
                        if fits(matrix,row_n,column_n,a):
                                matrix[row_n][column_n] = a
                        
                        else:
                                matrix[row_n][column_n] = a
                                return False 
                        
        