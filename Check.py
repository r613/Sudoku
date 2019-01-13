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
