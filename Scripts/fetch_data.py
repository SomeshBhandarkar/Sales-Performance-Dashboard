import pandas as pd 
import random
import requests
from datetime import datetime, timedelta

# fetching the product data from the fakestore API 
response = requests.get("fakestoreapi link that you can find online!") # change this!
products = response.json()

# setting parameter for the fake transactions 
num_transactions = 100000
regions = ["North", "South", "East", "West"]
start_date = datetime.today() - timedelta(days=1095)
end_date = datetime.today()

# now we need to calculate the transactions to spread it evenly 
days_range = (end_date - start_date).days
transactions_per_day = num_transactions // days_range

# now we need to generate the data
sales_data = []
order_counter = 100000
for day_offset in range(days_range):
    current_date = start_date + timedelta(days=day_offset)
    # Slight random variation in daily transactions
    todays_transactions = transactions_per_day + random.randint(-5, 5)

    for _ in range(max(0, todays_transactions)):
        product = random.choice(products)
        order_id = f"ORD{order_counter}"
        order_counter += 1
        quantity = random.randint(1, 5)
        price = product["price"]
        total_sales = round(price * quantity, 2)
        customer_id = f"CUST{random.randint(1000, 9999)}"
        region = random.choice(regions)

        sales_data.append({
            "Order ID": order_id,
            "Order Date": current_date.strftime("%Y-%m-%d"),
            "Product": product["title"],
            "Category": product["category"],
            "Price": price,
            "Quantity": quantity,
            "Total Sales": total_sales,
            "Customer ID": customer_id,
            "Region": region
        })

df_sales = pd.DataFrame(sales_data)
df_sales.to_csv("sales_data.csv", index=False)
print(f"created the sales data with {len(df_sales)} rows")
