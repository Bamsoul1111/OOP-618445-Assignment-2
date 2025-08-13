import uuid

class Product:
    def __init__(self, name, description, price):
        """สร้างออบเจกต์สินค้า"""
        self.__name = name                # private attribute
        self.__description = description  # private attribute
        self.__price = price             # private attribute
        self.__online_shop = None        # private attribute
    
    # Getter methods เพื่อเข้าถึง private attributes
    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property
    def price(self):
        return self.__price
    
    @property
    def online_shop(self):
        return self.__online_shop
    
    # Setter method สำหรับ online_shop
    @online_shop.setter
    def online_shop(self, shop):
        self.__online_shop = shop

class Customer:
    def __init__(self, name, email, address):
        """สร้างออบเจกต์ลูกค้า"""
        self.__name = name           # private attribute
        self.__email = email         # private attribute
        self.__address = address     # private attribute
        self.__cart = []             # private attribute - ตะกร้าสินค้า
        self.__past_orders = []      # private attribute - ประวัติการสั่งซื้อ
    
    # Getter methods
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def address(self):
        return self.__address
    
    @property
    def cart(self):
        return self.__cart
    
    @property
    def past_orders(self):
        return self.__past_orders

class OnlineShop:
    def __init__(self, name, url):
        """สร้างออบเจกต์ร้านค้าออนไลน์"""
        self.__name = name          # private attribute
        self.__url = url            # private attribute
        self.__products = []        # private attribute
    
    # Getter methods
    @property
    def name(self):
        return self.__name
    
    @property
    def url(self):
        return self.__url
    
    @property
    def products(self):
        return self.__products
    
    def add_product_to_shop(self, name, description, price):
        """เพิ่มสินค้าในร้าน"""
        product = Product(name, description, price)
        product.online_shop = self  # เชื่อมโยงสินค้ากับร้าน
        self.__products.append(product)
        return product
    
    def addingItemsToCart(self, customer, product, quantity):
        """เพิ่มสินค้าที่ลูกค้าเลือกไปยังตะกร้าสินค้า"""
        # ตรวจสอบว่าสินค้านี้เป็นของร้านนี้หรือไม่
        if product in self.__products:
            # เพิ่มข้อมูลสินค้าและจำนวนลงใน cart ของ customer
            cart_item = {
                'product': product,
                'quantity': quantity
            }
            customer.cart.append(cart_item)
            print(f"เพิ่ม {product.name} จำนวน {quantity} ชิ้น เข้าตะกร้าเรียบร้อย")
        else:
            print("สินค้านี้ไม่มีในร้านของเรา")
    
    def checkOut(self, customer):
        """ดำเนินการสั่งซื้อสินค้าทั้งหมดที่อยู่ในตะกร้าของลูกค้า"""
        if not customer.cart:
            print("ตะกร้าสินค้าว่างเปล่า")
            return None
        
        # คำนวณราคารวม
        total_price = 0
        for item in customer.cart:
            total_price += item['product'].price * item['quantity']
        
        # สร้าง order_id ที่เป็นเอกลักษณ์
        order_id = str(uuid.uuid4())[:8]
        
        # สร้างบันทึกการสั่งซื้อ
        order_record = {
            'order_id': order_id,
            'items': customer.cart.copy(),  # คัดลอกรายการสินค้า
            'total_price': total_price
        }
        
        # เพิ่มบันทึกเข้าไปใน past_orders
        customer.past_orders.append(order_record)
        
        # ล้างข้อมูลใน cart ของลูกค้าให้เป็นว่าง
        customer.cart.clear()
        
        print(f"สั่งซื้อสำเร็จ! Order ID: {order_id}")
        print(f"ยอดรวม: {total_price:.2f} วอน")
        
        return order_id
    
    def orderTracking(self, customer, order_id):
        """ตรวจสอบสถานะของรายการสั่งซื้อที่เคยสั่งไปแล้ว"""
        # ค้นหารายการสั่งซื้อจาก past_orders ของลูกค้า
        for order in customer.past_orders:
            if order['order_id'] == order_id:
                print(f"\n=== รายละเอียดคำสั่งซื้อ {order_id} ===")
                print("รายการสินค้า:")
                for item in order['items']:
                    product = item['product']
                    quantity = item['quantity']
                    subtotal = product.price * quantity
                    print(f"- {product.name} x{quantity} = {subtotal:.2f} วอน")
                print(f"ยอดรวม: {order['total_price']:.2f} วอน")
                print("สถานะ: จัดส่งเรียบร้อย")
                return
        
        print(f"ไม่พบคำสั่งซื้อ ID: {order_id}")

# --- ตัวอย่างการใช้งาน ---
if __name__ == "__main__":
    # สร้างร้านค้าออนไลน์
    shop = OnlineShop("NCT Comedy", "www.neocomadytiti.com")
    
    # เพิ่มสินค้าในร้าน
    album = shop.add_product_to_shop("Album Smootie", "Album ISTJ", 2738.0)
    goods = shop.add_product_to_shop("Cute Goods", "Hot Goods", 5328.16)
    
    # สร้างลูกค้า
    customer1 = Customer("Mr. Na Jaemin", "p_jaemin@email.com", "127 Nongdream Rd., Soul")
    
    # เพิ่มสินค้าเข้าตะกร้า
    shop.addingItemsToCart(customer1, album, 2)
    shop.addingItemsToCart(customer1, goods, 1)
    
    # ชำระเงิน
    order_id = shop.checkOut(customer1)
    
    # ตรวจสอบสถานะคำสั่งซื้อ
    if order_id:
        shop.orderTracking(customer1, order_id)