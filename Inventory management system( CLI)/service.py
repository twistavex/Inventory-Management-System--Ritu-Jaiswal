from product import Product
from file_handler import load_data ,save_data

class InventoryService:
    def __init__(self):
        self.products = [Product(**item) for item in load_data()]
        
    def add_product(self, product):
        self.products.append(product)
        self.save()
    
    def view_product(self):
        for product in self.products:
            print(product)
    
    def update_product(self, product_id , new_product):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                self.products[i] = new_product
            self.save()
    
    def delete_product(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]
        self.save()
    
    def save(self):
        save_data([item.to_dict() for item in self.products])              