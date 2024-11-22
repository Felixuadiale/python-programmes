class parrot:
    species="board"
    def __init__(self,name , age):
        self.name=name 
        self.age=age
    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    def dance(self):
        return"{} is now dancing".format(self.name)
blue=parrot("blue",10)
woo=parrot("woo",15)
print("Blue is a {} ". format(blue.species))
print("Woo is a {} ". format(woo.species))
print("{} is {} years old".format(blue.name,blue. age))
print("{} is {} years old".format(woo.name,woo. age))
print(blue.sing("Happy"))
print(blue .dance())