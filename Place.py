class Place:
    transactions = [None] * 20
    pos = 0
    mark = 0
    name = ""
    def __init__(self, name):
        self.name = name

    def addtransaction(self, transaction):
        self.transactions[self.pos] = transaction
        self.pos += 1

    def printplace(self):
        print(self.name)

    def addmark(self, mark):
        self.mark = mark