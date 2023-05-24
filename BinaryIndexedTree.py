class FenwickTree:


	def g(i):
		#toggle the lsb of i
		#lsb(i) = i & -i
		return i - (i & (-i))
		
	def h(i):
		i + (i & (-i))

	def __init__(arr):
		self.n = len(arr) + 1	
		self.bit = [0 for i in range(n)]
		for i in range(self.n):
			self.add(i, arr[i])
	
		
	def sum(r):
		result = 0
		r += 1
		while r > 0:
			result += self.bit[r]
			r = self.g(r)
		return result
		
	def sum(l, r):
		return self.sum(r) - self.sum(l-1)
	
	def add(index, delta):
		index += 1
		while index < self.n:
			self.bit[index] += delta
			index = self.h(index)
	