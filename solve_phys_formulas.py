"""============================================================================
The input is a file containing lines of the following form:
 
   equation_name arg1 ...

For example:

   energy 5.4 3.7 99
   something 7 280.01
   energy 88.94 73 21.2
   whizbang 83.34 14.34 356.43  139593.7801
   something .001 25

You must pass the name of the input file on the command-line.  Do not hard-code
the input file name in the source code.

You must validate the name of the physics equation and the number of arguments.
If the name of the equation is invalid, write an error message and skip to the
next line.  If the equation name is valid, but has the wrong number of
arguments, write an error message and skip to the next line.

If the equation name and number of arguments is correct, call the equation with
the arguments and print the answer like this:

physics_equation_name(arg1, arg2 ...) = answer
============================================================================"""

from physequations import grav_potential_energy, kin_energy, work_energy
from pprint import pprint

# print('<--checking equations hardcoded with rounding-->')
# print(grav_potential_energy(2, 6.4))
# print(round(grav_potential_energy(2, 6.4), 2))
# print(kin_energy(2, 5))
# print(work_energy(2, 5, 30))
# print(round(work_energy(2, 5, 30), 2))
# print()

def isint(s):
   """Checks to see if input is an interger"""
   try:
      int(s)
   except:
      return False
   return True


# string = 'this is a string'
# print(string.split())
# print()

"""logic: find if the index element is not an int then start a new line"""

f = open('resources/equations_input.txt', 'r')
flines = f.readlines()
# pprint(flines)

equations = []
for line in flines:
  spline = line.split()
  # print(spline)
  equations.append(spline)

# print('===> equations')
# pprint(equations)

for equation in equations:
  eqname = equation[0]
  # print(eqname)
  if eqname != 'grav_potential_energy' and eqname != 'kin_energy' and \
          eqname !='work_energy':
      print(f'{eqname} is not valid')
  # print(equation)



  numargs = len(equation) - 1
  if eqname == 'grav_potential_energy':
    if numargs != 2:
      print(f'Wrong number of arguments: {equation}')
    else:
      mass = float(equation[1])
      height = float(equation[2])
      ans = grav_potential_energy(float(equation[1]), float(equation[2]))
      # {mass, height} creates a tuple
      # ({mass}, {height}) is another way to format it
      print(f'{eqname}{mass, height} = {ans}')


  if eqname == 'kin_energy':
    if numargs != 2:
      print(f'Wrong number of arguments: {equation}')
    else:
      mass = float(equation[1])
      velocity = float(equation[2])
      ans = kin_energy(float(equation[1]), float(equation[2]))
      # {mass, velocity} creates a tuple
      # ({mass}, {velocity}) is another way to format it
      print(f'{eqname}{mass, velocity} = {ans}')
      

  if eqname == 'work_energy':
    if numargs != 3:
      print(f'Wrong number of arguments: {equation}')
    else:
      force = float(equation[1])
      displacement = float(equation[2])
      angle = float(equation[3])
      ans = work_energy(float(equation[1]), float(equation[2]), float(equation[3]))
      # {force, displacement, angle} creates a tuple
      # ({force}, {displacement}, {angle}) is another way to format it
      print(f'{eqname}{force, displacement, angle} = {ans}')




