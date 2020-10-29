import turtle
whiler = 1
a = turtle.Turtle()
a.width(1)
while whiler > 0 :
  W = int(input("Enter Width =>"))
  X = int(input("Enter X =>"))
  Y = int(input("Enter Y =>"))
  Clean = int(input("Clean or not? (0 or 1) =>"))
  if Clean == 1 :
    a.reset()
  a.width(W)
  a.goto(X, Y)
  print("done!")