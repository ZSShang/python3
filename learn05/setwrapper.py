# setwrapper.py
class Set:
	def __init__(self,value=[]):
		self.data = []
		self.concat(value)

	def intersect(self,other):
		res = []
		for x in self.data:
			if x in other:
				res.append(x)
		return Set(res)

	def union(self,other):
		res = self.data[:]
		for x in other:
			if not x in res:
				res.append(x)
		return Set(res)

	def concat(self,value):
		for x in value:
			if not x in self.data:
				self.data.append(x)

	def __len__(self):	return len(self.data)	#len(self)
	def __getitem__(self,key): return self.data[key] #self[i]
	def __and__(self,other): return self.intersect(other)	# self & other
	def __or__(self,other): return self.union(other) # self | other
	def __repr__(self): return 'Set:' + repr(self.data) # print()

x = Set([1,3,5,7])
print(x.union(Set([2,4,5,6,7])))
#Set:[1, 3, 5, 7, 2, 4, 6]

print(x | Set([2,4,6]))
#Set:[1, 3, 5, 7, 2, 4, 6]
