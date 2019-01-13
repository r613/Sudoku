from Check import check
from Create import create
from Input import Input


puzzle = create()

num1 = Input("Please enter the row of the space you would like to check: ")
num2 = Input("Please enter the column of the space you would like to check: ")
number = Input("Please enter the number you want to try to fit in: ")
#print puzzle
check(puzzle,num1-1,num2-1,number)

