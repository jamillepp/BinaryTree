class Level:
	matrix = []
	
class Node:

	value = None #Valor.
	father = None # Pai
	right = None #Filho direito.
	left = None #Filho esquerdo.
	depth = None #Profundiade em relação à raiz.

	def __init__(self, value, father, right, left, depth):
		self.value = value
		self.father = father
		self.right = right
		self.left = left
		self.depth = depth

	def MakeLevel( self, level, niv ): # Cria uma matriz que contém os valore em casa nível da árvore

		if( self.value == None ):
			# Preenche o nível atual e os próximos com espaço (questão estética)
			level.matrix[niv].append(' ')
			cont = 2
			for i in range( niv + 1, len( level.matrix ) ):
				for j in range( cont ):
					level.matrix[i].append(' ')
				cont = cont * 2

		else:
			level.matrix[niv].append( self.value )
			niv += 1
			if( niv > len( level.matrix ) - 1 ):
				return False
			self.left.MakeLevel( level, niv )
			self.right.MakeLevel( level, niv )

class Tree:

	root = None #Raiz.
	nodes = None #Quantidade de nós.
	height = None #Altura da árvore.
	level = [] # Matriz com os valores em cada nível
	
	def __init__(self):
		NoneItem = Node( None, None, None, None, 1 )
		self.root = Node( None, NoneItem, NoneItem, NoneItem, 0 )
		self.nodes = 0
		self.height = -1

	def Push(self, item ): #Pronto
	
		if( self.height == -1 ): # Se estiver vazia
		
			(self.root).value = item
			self.height+= 1
			self.nodes += 1
			
		else:
		
			nodeDepth = 0 #Contador para saber qual a profundidade do nó.
			push = False #Colocado = True ou False.
			i = self.root #Essa variável vai percorrer a árvore começando da raiz.

			while( push == False ):

				father = i
				NoneItem = Node( None, None, None, None, 0 )
				newItem = Node( item, father, NoneItem, NoneItem, 0 )

				if( i.left.value == None and item < i.value ):
				
					nodeDepth+= 1

					NoneItem.depth = nodeDepth + 1
					newItem.depth = nodeDepth

					i.left = newItem
					self.nodes += 1
					push = True

					if( self.height < nodeDepth ):
					
						self.height = nodeDepth
			
				elif ( i.right.value == None and item > i.value ):
				
					nodeDepth+= 1

					NoneItem.depth = nodeDepth + 1
					newItem.depth = nodeDepth

					i.right = newItem
					self.nodes+= 1
					push = True

					if( self.height < nodeDepth ):
					
						self.height = nodeDepth
			
				#Enquanto não encontrar um nó vazio para colocar o item novo:
				elif( (item > i.value) ):
				
					i = i.right
			
				elif( item < i.value ):
				
					i = i.left

				nodeDepth+= 1
		
	def ShowInfo(self): # Pronto

		print("\nINFORMAÇÕES:\n")
	
		print((self.root).value, " (ROOT)")
		print( self.height,  " (HEIGHT)")
		print( self.nodes, " (NODES)")

	def Show(self): # Precisa de ajustes na nos espaços que separam nos itens ( Se ela tem height > 2 )

		self.level = Level()
		self.level.matrix = []		

		for i in range( self.height + 1 ):

			self.level.matrix.append([])

		self.root.MakeLevel( self.level, 0 )

		print("\nÁRVORE BINÁRIA:\n")

		ext = len( self.level.matrix ) * 2 # Separador externo ( no começo e no fim de cada linha )

		inte = ext - 1 # Separador interno ( entre os nós )
		
		cont = ext // 2 # Variável para regular a subtração na variável inte ( o número subtraido vai mudar conforme o nível )

		for i in range( len( self.level.matrix ) ):

			print('|', end='')

			for k in range( ext ):
				print(" ",end='')

			for j in range( len( self.level.matrix[i]) ):

				if( i != 0 and j != 0):
					for t in range( inte ):
						print(" ",end='')

				print(self.level.matrix[i][j],end ='',sep='')

			for k in range( ext ):
				print(" ",end='')

			print('')
			ext = ext // 2
			if( i != 0 ):
				inte -= cont
				cont -= 2

	def Search(self,item): # Pronto

		node = self.root

		while( not(node.right.value == None and node.left.value == None) and node.value != item):
			if( item < node.value ):
				node = node.left
			elif( item > node.value ):
				node = node.right
		else:
			if(node.value == item):
				return node
			elif(node.right.value == None and node.left.value == None):
				print('Não encontrado')
				return False

	def Delet(self,item):

		NoneItem = Node( None, None, None, None, 0 )
		item = self.Search(item)

		if( item.right.value == None and item.left.value == None ): # Se for uma folha

			if( item.value > item.father.value ):

				item.father.right = NoneItem
				self.nodes -= 1
				print('\n-----------------------')
				print('\nITEM {} FOI DELETADO:'.format(item.value))
				self.Show()

			elif( item.value < item.father.value ):

				item.father.left = NoneItem
				self.nodes -= 1
				print('\n-----------------------')
				print('\nITEM {} FOI DELETADO:'.format(item.value))
				self.Show()

		for i in range(  len(self.level.matrix[ self.height ]) ) :

			if( self.level.matrix[ self.height ][i] != ' ' ):
				break
			elif( i == len(self.level.matrix[ self.height ]) - 1):
				self.level.matrix.pop()
				self.height -= 1

		self.ShowInfo()


# Criação da árvore

print('\n-----------------------')

tree = Tree()

tree.Push(5)
tree.Push(3)
tree.Push(4)
tree.Push(2)
tree.Push(8)
tree.Push(7)
tree.Push(9)

tree.Show()

tree.Delet(7)
tree.Delet(9)
tree.Delet(4)
tree.Delet(2)
