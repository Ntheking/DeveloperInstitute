class BankAccount():
	authenticated = False
	balance = 0
	username = "nw"
	password = "1234"
	def __init__(self, balanceSet):
		self.balance = balanceSet
	def deposit(self, addVal):
		if not self.authenticated:
			print("YOU LACK AUTHENTICATION")
		elif addVal > 0:
			self.balance += addVal
		else:
			print("MUST INSERT POSITIVE VALUE")
	def withdraw(self, subVal):
		if not self.authenticated:
			raise "NOT A VALID VALUE"
		elif subVal > 0:
			self.balance -= subVal
		else:
			print("NOT A VALID VALUE")
	def authenticate(self, username, password):
		if username == self.username and password == self.password:
			self.authenticated= True
		else:
			print("INVALID USERNAME OR PASSWORD")
class MinimumBalanceAccount(BankAccount):
	minBalance = 0
	def __init__(self, balanceSet, minBalance):
		super().__init__(balanceSet)
		self.minBalance = minBalance
	def withdraw(self, subVal):
		if not self.authenticated:
			print("YOU LACK AUTHENTICATION")
		elif subVal > 0 and self.balance - subVal >= minBalance:
			self.balance -= subVal
		else:
			print("NOT A VALID VALUE")
class ATM():
	current_tries = 0
	account_list = []
	try_limit = 0
	def __init__(self, account_list, try_limit):
		for acc in account_list:
			if not isinstance(acc, BankAccount):
				print("invalid account given")
				return
		self.account_list = account_list
		if try_limit < 0:
			raise "Should be positive"
			self.try_limit==2
		self.current_tries =0
		self.showmainmenu()
	def showmainmenu(self):
		while True:
			print('1: Log in')
			print('2: Exit')
			if int(input("Choose?"), 10) == 1:
				user = input("username?")
				pas = input("password?")
				self.logIn(user, pas)
			else:
				print("Goodbye")
				break
	def logIn(self, username, password):
		for x in self.account_list:
			if x.username == username and x.password == password:
				print("authenticated")
				x.authenticate(username, password)
				self.show_account_menu(x)
				return
		self.current_tries +=1
		if self.current_tries < self.try_limit:
			self.logIn(input("Username?"), input("Password?"))
	def show_account_menu(self, acc):
		while True:
			print("Balance: " + str(acc.balance))
			print('1: Deposit')
			print('2: Withdraw')
			print('3: Logout')
			val = int(input("Choose?"), 10)
			if val == 1:
				acc.deposit(int(input("How Much?"), 10))
			elif val == 2:
				acc.withdraw(int(input("How Much?"), 10))
			else:
				break
		self.showmainmenu()


account = [BankAccount(100), MinimumBalanceAccount(100, 0), BankAccount(100)]
hi = ATM(account, 2)


