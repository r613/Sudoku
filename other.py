def Input(text):
  try:
    return input(text)
  except:
    print "Nice try, Numbers only! Please try again"
    return Input(text)

def make_a_matrix():
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

