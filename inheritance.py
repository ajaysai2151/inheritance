class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name = name 
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_Save = price - deal_price
    def product_details(self):
        print("product : {}".format(self.name))
        print("price : {}".format(self.price))
        print("deal_price : {}".format(self.deal_price))
        print("ratings : {}".format(self.ratings))
        print("you_Save : {}".format(self.you_Save))
class Electronic_Items(Product):
    def set_warranty(self,warranty):
        self.warranty = warranty
    def display_electronic_item_details(self):
        self.product_details()
        print("warranty : {}".format(self.warranty))

e = Electronic_Items("laptop",35000,30000,4.2)
e.set_warranty(24)
e.display_electronic_item_details()