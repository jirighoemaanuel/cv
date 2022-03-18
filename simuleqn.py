message = """
Simultaneous eqn solver

     Ax + By = C
     Dx + Ey = F"""
print(message)

# a = int(input("A = "))
# b = int(input("B = "))
# c = int(input("C = "))
# d = int(input("D = "))
# e = int(input("E = "))
# f = int(input("F = "))

req_ver = ["A = ", "B = ", "C = ", "D = ", "E = ", "F = "]
v = {}  # v stores the variables needed for the calc.

while True: 
 for i in req_ver:
  print(i, end="")
  check = False
  while True:  # This block checks to make sure the userInput is an integer 
   try: 
    z = int(input())
    check = True
   except ValueError:
    print(f"Please input an interger value for {i[0]}")
    print(i, end="")
   if check:  # Break the checking loop after confirmation
    break
  v[i[0]] = z
 if len(v) == 6: # Break the entire loop after i got the required variables "v"
  break
  

Y = (v["F"] *v["A"]-v["D"]*v["C"])/(v["E"]*v["A"]-v["D"]*v["B"])
X = (v["B"] *v["F"]-v["E"]*v["C"])/(v["B"]*v["D"]-v["E"]*v["A"])
print(f"Y = {Y}\nX = {X}")

