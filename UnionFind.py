class UnionFind:
	def __init__(self, n):
		"""
		Create a union find data structure with nodes 0 through n.
		"""
		self.parent = [i for i in range(n)]
		self.size = [0 for i in range(n)]
		self.components = n
		self.n = n
		
	def find(self, ind):
		"""
		Return the root of a given node.
		"""
		if ind < 0 or ind >= self.n:
			raise IndexError('Out of bounds.')
			
		curPtr = ind
		while self.parent[curPtr] != curPtr:
			curPtr = self.parent[curPtr]
		ans = curPtr
		
		#Path Compression
		curPtr = ind
		while self.parent[curPtr] != curPtr:
			temp = self.parent[curPtr]
			self.parent[curPtr] = ans
			curPtr = temp
		return curPtr
		
	def union(self, ind1, ind2):
		"""
		Merge the two given components.
		"""
		if ind1 < 0 or ind2 < 0 or ind1 >= self.n or ind2 >= self.n:
			raise IndexError('Out of bounds.')
			
		p1 = self.find(ind1)
		p2 = self.find(ind2)
		
		if p1 == p2:
			return
			
		#Union by rank
		if self.size[p1] > self.size[p2]:
			self.parent[p2] = p1
			
		elif self.size[p2] > self.size[p1]:
			self.parent[p1] = p2
			
		else:
			self.parent[p2] = p1
			self.size[p2] += 1
			
		self.components -= 1
		
	def connected(self, ind1, ind2):
		if ind1 < 0 or ind2 < 0 or ind1 >= self.n or ind2 >= self.n:
			raise IndexError('Out of bounds.')

		return self.find(ind1) == self.find(ind2)
		
	def components(self):
		return self.components