class Product:
    def __init__(self,product_id,name,price,stock):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock
        
    def to_dict(self):
        return{
               "id": self.product_id,
               "name": self.name,
               "price": self.price,
               "stock": self.stock,
        }
    def __str__(self):
        return f"Product: {self.name} (ID: {self.product_id}) - Price: ${self.price}, Stock: {self.stock}"