import copy
class Vector (object):
	def __init__(self, vector):
		self.vector = vector

	def Index(self,lista1,num):
		try:
			return lista[num]
		except:
			return -1
		pass

	def ListToString(self):
		return "{}".format(self.vector)
	#==
	def IsEqual(self,a,res,lista1,lista2):
		res = 0
		for num in lista1:
			for num2 in lista2:
				if (num == num2):
					res = res+1
		if (res == a):
			return True
		return False
	#!=
	def IsNotEqual(self,res):
		return not(res)
	#Operador <<
	def OperatoriBtLeft(self,lista1):
		answer = 0
		cont = 0
		sent = []
		copyVectorcito = copy.deepcopy(lista1)
		for i in copyVectorcito:
			cont += 1			
			answer = i << cont
			sent.append(answer)
		return sent

	def OperatorBitRigth(self, lista1):
		answer = 0
		cont = 0
		sent = []
		copyVectorcito = copy.deepcopy(lista1)
		print(copyVectorcito)
		for i in copyVectorcito:
			print(i)
			cont += 1
			print(cont)			
			answer = i >> cont
			sent.append(answer)
		return sent	

	def main():	
		res = False
		Right =[]
		Left= []
		#num = 10
		lista1 = [1,2,3,4,5,6,7,8,9]
		lista2 = [1,2,3,4,5,6,7,8,9]
		vectorcito = Vector(lista1)
		vectorcito2 = Vector(lista2)
		a = len(lista1)
		res = vectorcito.IsEqual(a,res,lista1,lista2)
		res = vectorcito.IsNotEqual(res)
		print(res)
		Left = vectorcito.OperatoriBtLeft(lista1)
		for i in Left:
			print(i)
		print(vectorcito.Index(lista1,10))

#Inicio
if __name__ == '__main__':
    Vector.main()
    pass



