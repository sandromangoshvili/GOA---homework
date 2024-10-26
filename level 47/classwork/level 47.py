color = "Green"
try:
  print(color)
except NameError:
  print("Check the variable name")




  colors = ['Red', 'Yellow', 'Green']
try:
  print(colors[10])
except IndexError:
  print("Out of range")




try:
  print(len(5))
except NameError:
  print("Variable is not defined")
except TypeError:
  print("Not iterable")