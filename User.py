def creator():
    matrix = []
    print "Please enter the Sudoku Puzzle"
    for i in range(9):
        matrix.append(r_creator())
    return matrix
    
def r_creator():
    text = raw_input("-")
    row = []
    for piece in text.split(" "):
        for i in piece:
            row.append(int(i))
    return row