# instance variable
class shoppingmall:

    def __init__(self, category, size, type, color): # constructor
        # Instance variable
        self.category = category
        self.size = size
        self.type = type
        self.color = color

    def shoppingDetails(self):
       print(f"Customer Requirement is {self.category}, size is {self.size}, type is {self.type} and color is {self.color}")

# method variable
class operations:
    def fact(self):
        n = 5
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return f"factorical of {n} is: {fact}"

# obj = operations()
# print(obj.fact())

# static variable

class clientDetails:
    wel_msg = "Welcome to the Company"  # static variable
    def __init__(self, reqiruement, loaction, domain, duration): # constructor
        # Instance variable
        self.reqiruement = reqiruement
        self.loaction = loaction
        self.domain = domain
        self.duration = duration

    def clientInfo(self):
       print(f"Client Requirement is {self.reqiruement}, Working Location is {self.loaction}, Domain Details is {self.domain} and TimeFrame is {self.duration}")

# obj = clientDetails("ecom website", "Bengaluru", ".Net", "6 Months")
# obj.clientInfo()

