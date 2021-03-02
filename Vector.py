import copy
import random
class Vector (object):
	def __init__(self, vector):
		self.vector = vector

	def ListToString(self):
		return "{}".format(self.vector)

	def IsEqual(self):
		res = 0 
		print(lista)
		print(copyVectorcito)
		for num in lista:
			#print(num)
			for num2 in copyVectorcito:
				#print(num2)
				if (num == num2):
					res = res+1	
					print(res)
		if(res == num):
			print("It's Equal")
		else:
			print("Itsn't Equal")
	def OperatoriBtLeft(self, copyv):
		pass

	def OperatorBitRigth(self, copyv):
		pass
#Inicio
lista = [1,2,3,4,5,6,7,8,9]
vectorcito = Vector(lista)
copyVectorcito = copy.deepcopy(lista)
a = len(lista)
#print(a)
b = len(copyVectorcito)
#print(b)
vectorcito.IsEqual()

