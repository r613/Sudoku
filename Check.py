from Input import Input 

def check(puzzle,num1,num2,attempt):
  print "This number is able to go in the row: "
  print check_r(puzzle,num1,attempt)
  print "This number is able to go in the column: "
  print check_c(puzzle,num2,attempt)    

def check_r(puzzle,num1,attempt):
  pos = True
  for space in puzzle[num1]:
    if space == attempt:
      pos = False
  return pos


def check_c(puzzle,num2,attempt):
  pos = True
  for row in puzzle:
    if row[num2] == attempt:
      pos = False
  return pos


def check_b(puzzle,row_n,col_n,attempt):
  pos = True
  tlist = []
  box_row_n = (row_n/3)*3 #The  nubmer row that the box starts
  box_col_n = (col_n/3)*3 #The nubmer column that the box starts 
  for temp_rn in range(box_row_n,box_row_n + 3):
    for temp_cn in range(box_col_n,box_col_n +3):
      
      if puzzle[temp_rn][temp_cn] == attempt:
        pos = False
  return pos
