import copy
class Vector (object):
	def __init__(self, vector):
		self.vector = vector

	def ListToString(self):
		return "{}".format(self.vector)

	def IsEqual(self,res):
		res = 0
		for num in lista:
			for num2 in copyVectorcito:
				if (num == num2):
					res = res+1	
		print(res)
		return res
	def OperatoriBtLeft(self, copyv):
		pass

	def OperatorBitRigth(self, copyv):
		pass
#Inicio
res = 0
lista = [1,2,3,4,5,6,7,8,9]
vectorcito = Vector(lista)
copyVectorcito = copy.deepcopy(lista)
print(res)
vectorcito.IsEqual(res)
print(res)


