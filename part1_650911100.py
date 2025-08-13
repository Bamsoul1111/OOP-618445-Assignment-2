# สร้าง product_list เริ่มต้น (ว่าง)
product_list = []

def add_product(product_list):
    """เพิ่มสินค้าใหม่เข้าไปใน product_list"""
    # รับชื่อสินค้าจากผู้ใช้
    name = input("กรุณาป้อนชื่อสินค้า: ")
    
    # รับจำนวนสินค้าจากผู้ใช้และแปลงเป็น integer
    quantity = int(input("กรุณาป้อนจำนวนสินค้า: "))
    
    # สร้าง dictionary ที่มี key เป็น "name" และ "quantity"
    product_dict = {
        "name": name,
        "quantity": quantity
    }
    
    # เพิ่ม dictionary เข้าไปใน product_list
    product_list.append(product_dict)

def show_products(product_list):
    """แสดงรายการสินค้าทั้งหมดใน product_list"""
    print("Product List:")
    for i, product in enumerate(product_list, 1):
        print(f"{i}. {product['name']} - {product['quantity']} units")

# --- ตัวอย่างการทดสอบโปรแกรม ---
add_product(product_list)
add_product(product_list)
show_products(product_list)