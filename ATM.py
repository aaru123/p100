class Atm(object):
    def __init__(self, accontName, accountOwnersAge, accountCash):
      self.accontName = accontName
      self.accountOwnersAge = accountOwnersAge
      self.accountCash = accountCash
      
      
    def ispersonRich(self):
        if self.accountCash>100000:
            print('the person is rich')
        elif self.accountCash<1000:
            print("peron is poor")
        elif self.accountCash>1000 and self.accountCash<100000:
            print("person is neither poor and nor rich")
            
qwerty = Atm("aryan",'18',1000010)    
print(qwerty.accontName) 
print(qwerty.accountOwnersAge) 
print(qwerty.accountCash) 
print(qwerty.ispersonRich())       
