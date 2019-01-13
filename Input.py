def Input(text):
  try:
    return input(text)
  except:
    print "Nice try, Numbers only! Please try again"
    return Input(text)