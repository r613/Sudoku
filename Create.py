from Input import Input

def create():
  size_h = 9
  size_w = 9
  list = []
  for row_no in range(size_h): #we run one row at a time
    print "you can enter the puzzle in the code itself (there are instructions inside to see how), or you may just enter it here"
    print "Please enter 9 numbers you may enter a space between each group of numbers,  "
    list.append(row_creator())
  
  return fix_matrix(list)

def fix_matrix(matrix):
  print "This is the matrix you have entered:"
  Print(matrix)
  action = Input("If you would like to make any changes, enter the number of the row you would like to change, otherwise - enter 0.")
  if action == 0:
    return matrix
  if (action == 1) or (action == 1) or (action == 2) or (action == 3) or (action == 4) or (action == 5) or (action == 6) or (action == 7) or (action == 8) or (action == 9):
    matrix[action - 1] = row_creator()
    return fix_matrix(matrix)
  else:
    print "Your choice was invalid let's try again:\n "
    return fix_matrix(matrix)  

def row_creator():
  try:
    row_list = raw_input(": ").split(" ") # row_list would be a list the user enters (like 1,2,3) and then split by ',' into a list
    new_list = []
    for nums in row_list:
      for num in nums:
        new_list.append(int(num)) #turns the characters the user entered into integers (since the original list looks like ['1','2','3'] and the script doesn't return them as ints)
    return new_list
  except:
    print "There was an error, Let's try again! "
    return row_creator()
def Print(matrix):
  print '\n'
  r_Print(matrix,0)
  r_Print(matrix,1)
  r_Print(matrix,2)
  print "-----------------"
  
  r_Print(matrix,3)
  r_Print(matrix,4)
  r_Print(matrix,5)
  print "-----------------"
  r_Print(matrix,6)
  r_Print(matrix,7)
  r_Print(matrix,8)
  print '\n'
  
def r_Print(matrix,i):
  print str(matrix[i][0]) +" "+ str(matrix[i][1]) +" "+ str(matrix[i][2]) +"|"+ str(matrix[i][3]) +" "+ str(matrix[i][4]) +" "+ str(matrix[i][5]) +"|"+str(matrix[i][6]) +" "+ str(matrix[i][7]) +" "+ str(matrix[i][8])
