# def process_product_listing(product_name, product_price, discount=0, tax=0.07, wrap_character="*", **supplier_info):
#     product_name= product_name.strip().lower()
#     product_price=product_price - (product_price * discount)
#     final_price=product_price + (product_price * tax)
#     final_price=product_price
#     for key, value in supplier_info.items():
#         print(f"{key}:{value}")

def process_product_listing(product_name, product_price, discount=0, tax=0.07, wrapper_character='*',**supplier_info):
    product_name=product_name.strip().lower()
    initial_product_price=product_price - (product_price * discount)
    product_price=product_price + (product_price * tax)
    # getting the suppliers info
    brand=supplier_info.get("company", "unknown brand")
    origin=supplier_info.get("city","Global")
    header= f" {brand} | {origin}"
    border= wrapper_character * len(header)+4
    print(border)
    print(f"Product: {product_name}")
    print(border)
    print(f"product price: {product_price:.2f}")
    print(border)
    print(f"Discount {discount}%")
    print(border)
    print(f"Tax {tax}%")
    print(border)
    

    