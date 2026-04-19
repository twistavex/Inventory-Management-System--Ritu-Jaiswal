from service import InventoryService
from product import Product

sercice = InventoryService()

while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        new_product = Product(product_id, name, price, stock)
        sercice.add_product(new_product)
        print("Product added successfully!")
        
    elif choice == '2':
        sercice.view_product()
        
    elif choice == '3':
        product_id = input("Enter product ID to update: ")
        name = input("Enter new product name: ")
        price = float(input("Enter new product price: "))
        stock = int(input("Enter new product stock: "))
        updated_product = Product(product_id, name, price, stock)
        sercice.update_product(product_id, updated_product)
        print("Product updated successfully!")
        
    elif choice == '4':
        product_id = input("Enter product ID to delete: ")
        sercice.delete_product(product_id)
        print("Product deleted successfully!")
        
    elif choice == '5':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please try again.")