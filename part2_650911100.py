class Product:
    def __init__(self, name, quantity):
        """เมธอดสำหรับสร้างออบเจกต์ Product"""
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        """สร้างคลาส Store พร้อมกับ __products ที่เป็นลิสต์ว่าง"""
        self.__products = []  # private attribute
    
    def add_product(self, name, quantity):
        """เพิ่มสินค้าใหม่เข้าไปในร้าน"""
        # สร้างออบเจกต์จากคลาส Product
        new_product = Product(name, quantity)
        
        # เพิ่มออบเจกต์นั้นเข้าไปในลิสต์ __products
        self.__products.append(new_product)
    
    def show_products(self):
        """แสดงรายการสินค้าทั้งหมดที่อยู่ใน __products"""
        print("Product List:")
        for i, product in enumerate(self.__products, 1):
            print(f"{i}. {product.name} - {product.quantity} units")

# --- ตัวอย่างการทดสอบโปรแกรม ---
my_store = Store()
my_store.add_product("Perfume", 15)
my_store.add_product("Lipstick", 50)
my_store.add_product("Blush-on", 25)
my_store.show_products()
