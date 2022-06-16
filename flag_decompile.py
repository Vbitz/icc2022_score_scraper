import sys
import random

flag_value = int(sys.argv[1])

factors = [400,306,231,180,144,118,100,76,57,45,36,29,25]

max_challenges = 35 + 7 + 1 + 13

def test(fac):
	if sum(fac) > max_challenges:
		return False
	if sum([fac * count for fac, count in zip(factors, fac)]) != flag_value:
		return False
	return True

def random_factors():
	return [random.randint(0, 10) for _ in factors]

while True:
	r = random_factors()
	if test(r):
		print([a for a in zip(factors, r)])
# 	else:
# 		print("false")
