class multi:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __mul__(self, other):
		return self.a + other.a, self.b + other.b

x = multi(1, 2)
y = multi(2, 3)
z = x * y
print(z)
