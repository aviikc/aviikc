class Musicians:
    name = ""
    instrument = ""

    def __init__(self, sname, instr):
        self.name = sname
        self.instrument = instr

    def __repr__(self):
        return f'{self.name} plays {self.instrument}'


    def __del__(self):
        return f'{self.name} destroyed'




guy_1 = Musicians( "James Hetfield", "bass")
# guy_1.name = "James Hetfield"
guy_me = Musicians("Ozzy Osbourne", "Singer")


print(guy_1.name)
print(guy_1.instrument)

print(guy_me)
print(guy_1)
# print(type(guy_1))
# del guy_1
# print(guy_1.name)
# print(Musicians.name)

