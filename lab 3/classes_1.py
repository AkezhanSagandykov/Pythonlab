class MyString:
    def getString(self):
        self.name = input()
    def printString(self):
        print(self.name.upper())
temp = MyString()
temp.getString()
temp.printString()