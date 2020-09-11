def fatorial(n):
	if n < 0:
		return 0

	fat = 1
	i = 1
	while i <= n:
		fat = fat * i
		i = i + 1
	return fat

def test_fat0():
	assert fatorial(0) == 1

def test_fat1():
	assert fatorial(1) == 1

def test_fat4():
	assert fatorial(4) == 24

def test_fat5():
	assert fatorial(5) == 120

def test_fat6():
	assert fatorial(-10) == 0