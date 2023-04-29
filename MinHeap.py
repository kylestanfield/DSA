class MinHeap:
	def __init__(self, arr):
		"""
		Given an array, turn it into a heap with the min-heap property:
		At every node, the value of that node is less than or equal to
		the value of all of its children.
		O(N)
		"""
		self.arr = arr
		self.n = len(arr)
		self.build_min_heap()
	
	def left(self, ind):
		"""
		Given an index of the heap, return the index of the left child.
		O(1)
		"""
		return 2*ind + 1
		
	def right(self, ind):
		"""
		Given an index of the heap, return the index of the right child.
		O(1)
		"""
		return 2*ind + 2
		
	def parent(self, ind):
		"""
		Given an index of the heap, return the index of the parent.
		O(1)
		"""
		return ind//2
		
	def build_min_heap(self):
		"""
		Rearrange the internal array so that the min heap property
		is satisfied.
		O(N)
		"""
		if self.n <= 1:
			return
		
		for i in reversed(range(self.n//2)):
			self.min_heapify(i)
			
	def min_heapify(self, ind):
		"""
		Given a subtree of the heap, fix any errors in the subheap.
		We assume that the left and right children satisfy
		the min heap property.
		O(lg N)
		"""
		l = self.left(ind)
		r = self.right(ind)
		
		if l >= self.n:
			return
			
		if r >= self.n:
			if self.arr[l] < self.arr[ind]:
				temp = self.arr[l]
				self.arr[l] = self.arr[ind]
				self.arr[ind] = temp
			return
			
			
		if self.arr[ind] < self.arr[l] and self.arr[ind] < self.arr[r]:
			return 
			
		if r >= self.n:
			if self.arr[l] < self.arr[ind]:
				temp = self.arr[l]
				self.arr[l] = self.arr[ind]
				self.arr[ind] = temp
			else:
				pass
		
		elif self.arr[l] < self.arr[r]:
			temp = self.arr[l]
			self.arr[l] = self.arr[ind]
			self.arr[ind] = temp
			self.min_heapify(l)
			
		else:
			temp = self.arr[r]
			self.arr[r] = self.arr[ind]
			self.arr[ind] = temp
			self.min_heapify(r)
			
	def min(self):
		"""
		Return the minimum element in the heap.
		O(1)
		"""
		if not self.n:
			raise IndexError('The heap is empty.')
		
		return self.arr[0]
		
	def extract_min(self):
		"""
		Pop out the minimum element and return it.
		O(lg N)
		"""
		if not self.n:
			raise IndexError('The heap is empty.')
		
		temp = self.arr[0]
		self.arr[0] = self.arr[self.n-1]
		self.n -= 1
		self.arr.pop()
		self.min_heapify(0)
		return temp
		
	def insert(self, val):
		"""
		Add the new value into the heap.
		O(lg N).
		"""
		self.arr.append(val)
		temp = self.n
		self.n += 1
		
		while temp != 0:
			p = self.parent(temp)
			self.min_heapify(p)
			temp = p
			
	def increase_key(self, old_val, new_val):
		"""
		Change the value of a key in the heap, if it exists.
		If there are multiple nodes with the same value, only one
		will be changed.
		O(N)
		"""
		if not self.n:
			raise IndexError('The heap is empty.')
			
		if new_val == old_val:
			return
		
		ind = None
		for i in range(self.n):
			if self.arr[i] == old_val:
				ind = i
		if ind == None:
			raise ValueError('That key does not exist in the heap.')

		if new_val < old_val:
			self.arr[ind] = new_val
			temp = ind
			while temp != 0:
				p = self.parent(temp)
				self.min_heapify(p)
				temp = p
		else:
			self.arr[ind] = new_val
			self.min_heapify(ind)
		
	def sort(self):
		"""
		Return a sorted array with every element in the heap.
		O(NlgN)
		"""
		sorted_arr = []
		while self.n:
			sorted_arr.append(self.extract_min())
		return sorted_arr
		
	def __str__(self):
		"""
		Return a string representation of the heap.
		O(N)
		"""
		q = [0]
		ind = 0
		s = ''
		while ind < self.n:
			it = q[ind]
			s += str(self.arr[it]) + ' '
			ind += 1
			q.append(self.left(it))
			q.append(self.right(it))
		return s[:-1]
	
			
	def __repr__(self):
		return self.__str__()