class product:
    def __init__(self,name=None,color=None,prize=None):
            self.name=name
            self.color=color
            self.prize=prize
    def info(self):
            return (self.prize)
tomato=product()
tomato.name="tomato"
tomato.color="czerwony"
tomato.prize= 4.56

turnip=product()
turnip.name="turnip"
turnip.color="white"
turnip.prize= 5.65


user_input = raw_input("write the name of one products from the list and I will tell you how much it costs [tomato,turnip]:")

print(eval(user_input).info())