import pandas as pd
import random
from faker import Faker

fake = Faker()
dates = pd.date_range(start="2023-01-01", end="2023-03-31", freq="D")
products = ["Laptop", "Phone", "Shirt", "Shoes"]
categories = ["Electronics", "Clothing"]
regions = ["Zurich", "Geneva", "Bern"]

data = {
    "Date": [random.choice(dates) for _ in range(200)],
    "Product": [random.choice(products) for _ in range(200)],
    "Category": [random.choice(categories) for _ in range(200)],
    "Region": [random.choice(regions) for _ in range(200)],
    "Revenue": [random.randint(50, 1500) for _ in range(200)],
    "Units_Sold": [random.randint(1, 15) for _ in range(200)]
}
df = pd.DataFrame(data)
df.to_csv("data/sales_data.csv", index=False)
print("Dummy-Daten erstellt: data/sales_data.csv")