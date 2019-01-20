from Input import Input
def create():
  size_h = 9
  size_w = 9
  list = []
  for row_no in range(size_h): #we run one row at a time
    print "Please enter 9! numbers with a space seperating each group of 3  "
    list.append(row_creator())
  return list

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