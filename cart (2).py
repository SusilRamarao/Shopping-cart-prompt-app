class Item(Customer):
	def Add_New_Item(self, name, price):
		self.item = name
		self.price = price
		print "The added item is "
		print str(name) + str(price)

	def __init__(self):
		self.item = ""
		self.price = 0


class Customer(object):



	def Add_Rem_Cart(self, task):
		self.item = ""

		if task == "add":
			
			print "Which item you would like to add"
			print "1.Wheat"
			print "2.Rice"
			print "3.Leaves"
			self.item = str(raw_input())
			print self.item
			self.cart.Add_Rem_Items("add", self.item)
			self.inventory.Add_Remove_Inventory_Item("rem", self.item)
		else:
			print "Which item to be removed"
			self.item = raw_input()
			self.cart.Add_Rem_Items("rem", self.item)
			self.inventory.Add_Remove_Inventory_Item("add", self.item)

	def Add_Rem_invent(self, task):

		self.item = ""

		if task == "add":
			
			print "Which item you would like to add"
			print "1.Wheat"
			print "2.Rice"
			print "3.Leaves"
			self.item = str(raw_input())
			print self.item
			self.inventory.Add_Remove_Inventory_Item(self.item, "add")
		else:
			print "Which item to be removed"
			self.item = raw_input()
			self.inventory.Add_Remove_Inventory_Item(self.item, "rem")


	def Menu(self):
		print "Welcome mr." + self.name

		print "Please enter the item you want to buy"
		print " Enter the options"
		choice = 0
		while choice != 5:
			print """
			      1. View Inventory
			      2. Add/Remove inventory
			      3. Add to cart
			      4. Remove Cart
			      5. View Cart
			      6. Exit
			      """
			choice = input()
			if choice == 1:
				self.inventory.View_Inventory()

			elif choice == 2:

				self.Add_Remove_Inventory_Item()
	
			elif choice == 3:
				self.Add_Rem_Cart("add")
			
			elif choice == 4:
				self.Add_Rem_Cart("rem")

			elif choice == 5:
				self.cart.View_Cart()

			else:
				"Thank you !!!"
				break

			

	def __init__(self,name):
		self.name = name
		self.cart = Cart()
		self.inventory = Inventory()
		self.item = Item()
		self.Menu()

#def __init__(self):
#	print "Shopping Cart"
#	print "Hello"
	



class Cart(Customer):

	def __init__(self):
		self.wheat = 0
		self.rice = 0
		self.leaves = 0
		self.item = ""

	


	def Add_Rem_Items(self, task, goods):
		self.item = str(goods)
		print str(goods) + "Hello"
		
		if task == "rem":
			if self.item == "wheat":
				self.wheat -= 1

			elif self.item == "rice":
				self.rice -= 1
			else:
				self.leaves -= 1
		else:
			if str(self.item) == "wheat":
				self.wheat += 1

			elif str(self.item) == "rice":
				self.rice += 1
			elif str(self.item) == "leaves":
				self.leaves += 1
			else:
				print self.item
				print "No such item"
			

	def View_Cart(self):
		print "Wheat" + str(self.wheat)
		print "Rice" + str(self.rice)
		print "Leaves" + str(self.leaves)

class Inventory(Customer):
	def __init__(self):
		self.wheat = 10
		self.rice = 10
		self.leaves = 10
	def View_Inventory(self):
		print self.wheat
		print self.rice
		print self.leaves
	def Add_Remove_Inventory_Item(self, task, item):
		if task == "rem":
			if item == "wheat":
				self.wheat -= 1

			elif item == "rice":
				self.rice -= 1
			else:
				self.leaves -= 1
		else:
			if item == "wheat":
				self.wheat += 1

			elif item == "rice":
				self.rice += 1
			else:
				self.leaves += 1



raj = Customer("Raj")
raj.Menu()

#print "Hello, what item you would like to buy"
#print "The available inventory are"
