class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    def withdraw(self, money):
    	if money > self.balance:
    		raise ValueError("not enough money")
    	else:
	    	self.balance -= money
	    	return "{} has {}.".format(self.name, self.balance)
    def check(self, name, money):
    	if name.balance < money:
    		raise ValueError("not enough money")
    	if name.checking_account == False:
    		raise ValueError("cant checking_account")
    	else:
    		self.balance += money
    		name.balance -= money
    		return "{} has {} and {} has {}.".format(self.name, self.balance, name.name, name.balance)
    def add_cash(self, money):
    	self.balance += money
    	return "{} has {}.".format(self.name, self.balance)