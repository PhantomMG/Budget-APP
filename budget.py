class Category:

    def __str__(self):
        stringOut = self.name.center(30, "*")+"\n"

        for element in self.ledger:
            stringOut += element["description"][:23].ljust(23) + str(
                "{:.2f}".format(round(element["amount"], 2)))[:7].rjust(7) + "\n"
        stringOut += "Total: "+str(self.get_balance())

        return stringOut

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description):
        self.ledger.append({"amount": float(amount), "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.deposit(-float(amount), description)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for dep in self.ledger:
            balance += dep["amount"]
        return balance
    def get_spent_balance(self):
        balance = 0
        for dep in self.ledger:
          if dep["amount"]<=0:
            balance += dep["amount"]
        return balance
      
    def transfer(self, amount, anotherCategory):
        if self.check_funds(amount):
          self.withdraw(amount, f"Transfer to {anotherCategory.name}")
          anotherCategory.deposit(amount, f"Transfer from {self.name}")
          return True
        else:
          return False
          
          
    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True


def create_spend_chart(categories=[]):
    bar_chart=""
    total = 0
    cats = []
    bar_chart+="Percentage spent by category\n"
    print("Percentage spent by category")
    for category in categories:
        
        total += category.get_spent_balance()
        cats.append({"category":category.name,
                    "balance":category.get_spent_balance()})
    for i in range(len(cats)):
        
        cats[i]["percBalance"] = (cats[i]["balance"]/total)*100


    for i in range(100, -10, -10):
        bar_chart+=(str(i)+"|").rjust(4)
        print((str(i)+"|").rjust(4), end="")
        for cat in cats:
            cat["percBalance"]=round(cat["percBalance"])
            if cat["percBalance"] >= i:
                bar_chart+=" o "
                print(" o ", end="")
            else:
                bar_chart+="   "
                print("   ", end="")
        bar_chart+=" \n"
        print("\n", end="")
    bar_chart+="    "
    print("    ", end="")
    bar_chart+="---"*len(cats)+"-\n"
    print("---"*len(cats)+"-")

    catLength = 0
    catName = []
    for cat in cats:
        if catLength <= len(cat["category"]):
            catLength = len(cat["category"])
        catName.append(cat["category"])
    for i in range(catLength):
        bar_chart+="    "
        print("    ", end="")
        for j in catName:
            if j[i:i+1] != "":
                bar_chart+=" "+j[i:i+1]+" "
                print(" "+j[i:i+1]+" ", end="")
            else:
                bar_chart+="   "
                print("   ", end="")
        bar_chart+=" \n"
        
        print()
    bar_chart=bar_chart[:-1]

    return bar_chart