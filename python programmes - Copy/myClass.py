class myClass:
    __privateVar =27
    def __privMeth (self):
          print("i'm inside class myClass")
    def hello(self):
          print ("Private Variable value :",myClass.__privateVar)

foo=myClass()
foo.hello()
foo.__privMeth()