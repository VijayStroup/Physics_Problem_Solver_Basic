import math

def close(expected, actual, maxerror):
	'''checks to see if the actual number is within expected +- maxerror.'''
	low = expected - maxerror
	high = expected + maxerror
	if actual >= low and actual <= high:
		return True
	else:
		return False

def grav_potential_energy(mass, height, gravity=9.81):
	'''calculate potential energy given mass and height. Mass in
	   kilograms and height in meters.'''
	gp_energy = mass * height * gravity
	return gp_energy

def kin_energy(mass, velocity):
	'''calculate kinetic energy given mass and velocity. Mass in
	   kilograms and velocity in meters per second.'''
	k_energy = .5 * mass * velocity ** 2
	return k_energy

def work_energy(force, displacement, angle):
	'''calculate work energy given force, displancement,
	   and angle. Force in newtons, displacement in meters, angle in degrees.'''
	anglerad = math.radians(angle)
	cos = math.cos(anglerad)
	w_energy = force * displacement * cos
	return w_energy

'''=============================================================================
                                    Tests
============================================================================='''

if __name__ == '__main__':
	def check(funcname, args, expected, ans, maxerror):
		if not close(expected, ans, maxerror):
			print(f'{funcname}({args}) = {ans} should = {expected}')

	print(close(10, 11.1, 1))
	print(close(100, 100.001, .01))
	print(close(-10, -11.01, 1))
	print(close(84756, 84300.2, 500.5))

	#gravitional potential energy tests
	ans = grav_potential_energy(3.00, 7.00)
	check('grav_potential_energy', '3.00, 7.00', 206.01, ans, 0.00000000000000000000000001)

	ans = grav_potential_energy(2.00, 5.00)
	check('grav_potential_energy', '2.00, 5.00', 98.1, ans, 0.01)

	#kinetic energy tests
	ans = kin_energy(2, 6.55)
	check('kin_energy', '2, 6.55', 42.90, ans, 0.01)

	ans = kin_energy(5.65, 10)
	check('kin_energy', '5.65, 10', 282.5, ans, 0.1)

	#work energy tests
	ans = work_energy(500, 10, 0)
	check('work_energy', '500, 10, 0', 5000.0, ans, 0.1)

	ans = work_energy(150, 50, 45)
	check('work_energy', '150, 50, 45', 5303.30, ans, 0.01)
