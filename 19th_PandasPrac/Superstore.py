import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = [
    ("Office Chair", "Furniture", 125.00),
    ("Laptop", "Technology", 850.00),
    ("Printer", "Technology", 220.00),
    ("Notebook", "Office Supplies", 8.50),
    ("Desk", "Furniture", 300.00),
    ("Stapler", "Office Supplies", 12.00),
    ("Monitor", "Technology", 275.00),
    ("Paper", "Office Supplies", 6.00),
    ("Bookshelf", "Furniture", 180.00),
    ("Keyboard", "Technology", 45.00),
]

regions = ["East", "West", "Central", "South"]
states = ["California", "Texas", "New York", "Florida", "Illinois"]
customers = ["John Smith", "Mary Johnson", "Robert Brown", "Linda Davis", "James Wilson"]

orders = []
supplies = []

start_date = datetime(2024, 1, 1)

for i in range(1, 401):
    product, category, price = random.choice(products)
    quantity = random.randint(1, 10)
    order_date = start_date + timedelta(days=random.randint(0, 365))
    sales = round(price * quantity, 2)
    discount = round(random.choice([0, 0.05, 0.10, 0.15, 0.20]), 2)
    profit = round(sales * (1 - discount) * random.uniform(0.08, 0.30), 2)

    orders.append({
        "Order ID": f"ORD-{i:04d}",
        "Order Date": order_date.date(),
        "Customer Name": random.choice(customers),
        "Product Name": product,
        "Category": category,
        "Region": random.choice(regions),
        "State": random.choice(states),
        "Quantity": quantity,
        "Sales": sales,
        "Discount": discount,
        "Profit": profit,
    })

    supplies.append({
        "Supply ID": f"SUP-{i:04d}",
        "Supply Date": order_date.date(),
        "Supplier": f"Supplier {random.randint(1, 20)}",
        "Product Name": product,
        "Category": category,
        "Warehouse": f"Warehouse {random.randint(1, 8)}",
        "Units Supplied": random.randint(10, 100),
        "Unit Cost": round(price * random.uniform(0.45, 0.75), 2),
        "Reorder Level": random.randint(10, 40),
        "Stock Status": random.choice(["In Stock", "Low Stock", "Pending"]),
    })

orders_df = pd.DataFrame(orders)
supplies_df = pd.DataFrame(supplies)

output_file = "Superstore_Orders_Supplies.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    orders_df.to_excel(writer, sheet_name="Orders", index=False)
    supplies_df.to_excel(writer, sheet_name="Supplies", index=False)

print(f"Created: {output_file}")