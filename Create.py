from Input import Input

def create():
  size_h = 3
  size_w = 3
  list = []
  for row in range(size_h):
    tlist = []

    for row in range(size_w):
      number = Input("Enter a number: ")
      tlist.append(number)
    list.append(tlist)
  return list
