# Physics Problem Solver Basic
### A script that will use basic physics formulas to solve equations.
#### Project Description:
>The input is a file containing lines of the following form:
> 
>   equation_name arg1 ...
>
>For example:
>
>   energy 5.4 3.7 99
>   something 7 280.01
>   energy 88.94 73 21.2
>   whizbang 83.34 14.34 356.43  139593.7801
>   something .001 25
>
>You must pass the name of the input file on the command-line.  Do not hard-code
>the input file name in the source code.
>
>You must validate the name of the physics equation and the number of arguments.
>If the name of the equation is invalid, write an error message and skip to the
>next line.  If the equation name is valid, but has the wrong number of
>arguments, write an error message and skip to the next line.
>
>If the equation name and number of arguments is correct, call the equation with
>the arguments and print the answer like this:
>
>physics_equation_name(arg1, arg2 ...) = answer

A script that will use basic physics formulas to solve work, gravitional, and kinetic energy problems when given certain information such as height, force, mass, ect.
Pretty in-dept project for my level as I needed help on parts of the program.  It took some days, but it is finally done.

When you run the program, it should output something like this:
```python
grav_potential_energy(1.0, 2.0) = 19.62
kin_energy(5.0, 20.0) = 1000.0
grav_potential_energy(5.0, 10.0) = 490.5
grav_potential_energy(6.6, 20.35) = 1317.5811
work_energy(10.0, 5.0, 0.0) = 50.0
Wrong number of arguments: ['grav_potential_energy', '4', '5', '6']
fake_formula is not valid
kin_energy(10.0, 2.0) = 20.0
Wrong number of arguments: ['kin_energy', '2', '0', '1']
kin_energy(0.0, 200.0) = 0.0
grav_potential_energy(10.0, 20.293) = 1990.7433
grav_potential_energy(0.0, 2.0) = 0.0
dummy_formula is not valid
nsl_force is not valid
kin_energy(30.0, 50.0) = 37500.0
Wrong number of arguments: ['grav_potential_energy', '10', '20', '30', '40', '50']
grav_potential_energy(5.5, 50.0) = 2697.75
grav_potential_energy(10.0, 20.0) = 1962.0
Wrong number of arguments: ['grav_potential_energy', '20', '20', '20']
mans_not_hot is not valid
quick_maths is not valid
work_energy(10.0, 20.2378, 30.0) = 175.26448916708713
kin_energy(204.24, 29.2) = 87071.5968
kin_energy(5.348, 10.2399) = 280.38374607474003
kin_energy(20.2, 1.2) = 14.543999999999999
grav_potential_energy(920.28, 294.249) = 2656464.3179532
Wrong number of arguments: ['work_energy', '20.238', '1']
Wrong number of arguments: ['kin_energy', '20', '20', '20', '20']
py_formula is not valid
circular_motion is not valid
work_energy(20.0, 30.0, 90.0) = 3.6739403974420595e-14
grav_potential_energy(2498.2489, 24894.24) = 610103595.5010563
grav_potential_energy(10000.0, 0.0) = 0.0
sublime_text is not valid
kin_energy(90.0, 20.0) = 18000.0
vijay_stroup is not valid
work_energy(0.0, 20.0, 0.0) = 0.0
grav_potential_energy(1.0, 1.0) = 9.81
kin_energy(1.2, 2.1) = 2.646
Wrong number of arguments: ['work_energy', '20', '30', '20', '10']
```
