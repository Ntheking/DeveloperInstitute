import random
class Gene():
	val = 0
	def __init__(self):
		self.val = random.randint(0,1)
	def mutate(self, prob):
		#print(prob)
		if self.val == 1:
			return 0
		r = random.randint(0, prob)
		#print(r)
		if r == 0:
			self.val = random.randint(0,1)
			print("YOU HAVE MUTATED")
			return -1
		return 0

class Chromosome():
	genes = []

	def __init__(self):
		for i in range(0,10):
			self.genes.append(Gene())
	def mutate(self, prob):
		for gene in self.genes:
			if gene.mutate(prob) == -1:
				return -1
		return 0
	def checkWin(self):
		for gene in self.genes:
			if gene.val == 0:
				return False
		return True

class DNA():
	chromosomes = []

	def __init__(self):
		for i in range(0,10):
			self.chromosomes.append(Chromosome())
	def mutate(self, prob):
		for chrom in self.chromosomes:
			if chrom.mutate(prob) == -1:
				return -1
		return 0
	def checkWin(self):
		for chrom in self.chromosomes:
			if chrom.checkWin() == False:
				return False
		return True
class Organism():
	iterations = 1;
	prob = 100;
	dnaObj = DNA()
	def __init__(self):
		self.prob = int(input("How likely is a mutation?"),10)
		# if self.prob > 2000000:
		# 	print("Probability is too big")
		# 	return
		self.test()
	def test(self):
		while not self.dnaObj.checkWin():
			self.dnaObj.mutate(self.prob)
			self.iterations += 1
		print(self.iterations)


test = Organism()