class Level: # Matriz para guardar os itens da ávore
	matrix = [] # ( Era necessário um ponteiro :/ )

class Node:

	value = None #Valor.
	right = None #Filho direito.
	left = None #Filho esquerdo.
	depth = None #Profundiade em relação à raiz.

	def __init__(self, value, right, left, depth):
		self.value = value
		self.left = left
		self.right = right
		self.depth = depth

	def CleanNone(self, level, heightTree):

		if( self.depth > (len( level.matrix ) - 1) ):

			while( (len( level.matrix ) - 1) != self.depth ):
				level.matrix.append( [] )

		if( self.value != '-' and self.depth != heightTree):
			if( (self.left != None or self.right != None) ):

				if( self.left == None ):
					depth = self.depth + 1
					newNode = Node( '-', None, None, depth)
					self.left = newNode

				if( self.right == None ):
					depth = self.depth + 1
					newNode = Node( '-', None, None, depth)
					self.right = newNode

				self.left.CleanNone( level, heightTree )
				self.right.CleanNone( level, heightTree )

			if(self.left == None and self.right == None ):

				depth = self.depth + 1
				newNode = Node( '-', None, None, depth)
				self.left = newNode
				self.right = newNode

				self.left.CleanNone( level, heightTree )
				self.right.CleanNone( level, heightTree )
				

		level.matrix[self.depth].append( self.value )






class Tree:
	root = None #Raiz.
	nodes = None #Quantidade de nós.
	height = None #Altura da árvore.
	level = [] # Matriz com os valores em cada nível
	
	def __init__(self):
		self.root = Node( None, None, None, 0 )
		self.nodes = 0
		self.height = -1

	def Push(self, item ):
		
		if( self.height == -1 ): # Se estiver vazia
		
			(self.root).value = item
			self.height+= 1
			self.nodes += 1

			self.level.append( [self.root.value] )
	
		else:
		
			nodeDepth = 0 #Contador para saber qual a profundidade do nó.
			push = False #Colocado = True ou False.
			i = self.root #Essa variável vai percorrer a árvore começando da raiz.

			while( push == False ):

				newItem = Node( item, None, None, 0 )

				if( (i.left == None or i.left.value == '-' ) and item < i.value ):
				
					nodeDepth+= 1

					if( nodeDepth > (len( self.level ) - 1) ):
						while( (len( self.level ) - 1) != nodeDepth ):
							self.level.append( [] )

					newItem.depth = nodeDepth
					i.left = newItem
					self.nodes += 1
					push = True
					self.level[ nodeDepth ].append( newItem.value )
					if( self.height < nodeDepth ):
					
						self.height = nodeDepth
				
			
				elif ( (i.right == None or i.right.value == '-') and item > i.value ):
				
					nodeDepth+= 1

					if( nodeDepth > (len( self.level ) - 1) ):
						while( (len( self.level ) - 1) != nodeDepth ):
							self.level.append( [] )

					newItem.depth = nodeDepth
					i.right = newItem
					self.nodes+= 1
					push = True
					self.level[ nodeDepth ].append( newItem.value )
					if( self.height < nodeDepth ):
					
						self.height = nodeDepth
				
			
				#Enquanto não encontrar um nó vazio para colocar o item novo:
				elif( (item > i.value) ):
				
					i = i.right
					nodeDepth+= 1

					if( nodeDepth > (len( self.level ) - 1) ):
						while( (len( self.level ) - 1) != nodeDepth ):
							self.level.append( [] )
			
				elif( item < i.value ):
				
					i = i.left
					nodeDepth+= 1

					if( nodeDepth > (len( self.level ) - 1) ):
						while( (len( self.level ) - 1) != nodeDepth ):
							self.level.append( [] )
		
			

	def ShowInfo(self): # Pronto

		print("\nINFORMAÇÕES:\n")
	
		print((self.root).value, " (ROOT)")
		print( self.height,  " (HEIGHT)")
		print( self.nodes, " (NODES)")


	def Show(self): # Precisa de ajustes na nos espaços que separam nos itens
		
		self.level = Level()

		self.root.CleanNone( self.level, self.height ) # Limpar nós vazios e trocar por '-' (questão estética)

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

	


tree = Tree()

tree.Push(8)
# tree.Push(4)
tree.Push(12)
tree.Push(2)
tree.Push(6)
# tree.Push(10)
# tree.Push(14)
# tree.Push(1)
# tree.Push(3)
# tree.Push(5)
# tree.Push(7)
# tree.Push(9)
# tree.Push(11)
# tree.Push(13)
# tree.Push(15)
tree.ShowInfo()

tree.Show()
