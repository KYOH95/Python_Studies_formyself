class COFFEE:
    def __init__(self, name, price, milk, flv_shot):
        self.name = name
        self.price = price
        self.milk = milk
        self.flv_shot = flv_shot
    
    def show_info(self):
        print("name:\t",self.name)
        print("price:\t",self.price)
        print("milk:\t",self.milk)
        print("flv_shot:",self.flv_shot)
    
    def set_name(self, name):
        self.name = name

    # def __del__(self):
    #     print("delete ", self.name, " instence")

coffee1 = COFFEE("Americano","3.00","No","No")
coffee2 = COFFEE("Latte","4.00","Whole","No")
coffee3 = COFFEE("C.M","5.00","Whole","C.M.")
coffee1.set_name("Hot tea")
coffee1.show_info()
coffee2.show_info()
coffee3.show_info()
