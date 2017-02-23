def add(a, b):
	print 'addind %d + %d' % (a, b)
	return a + b

def subtract(a, b):
	print 'subtract %d - %d' % (a, b)
	return a - b

def mutiply(a, b):
	print 'multiplying %d * %d' % (a, b)
	return a * b

def divide(a, b):
	print 'diving %d / %d' % (a, b)
	return a / b

print 'let\'s do some math with just functions!'

age = add(30, 5)
height = subtract(78, 4)
weight = mutiply(90, 2)
iq = divide(100, 2)

print 'age: %d, height: %d, weight: %d, iq: %d' % (age, height, weight, iq)

# a puzzle for the extra credit, type it in anyway.
print 'here is apuzzle.'

what = add(age,subtract(height, mutiply(weight, divide(iq, 2))))

print 'that becomes:', what, 'can you do it by hand?'