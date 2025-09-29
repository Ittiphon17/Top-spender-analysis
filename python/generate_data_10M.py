import pandas as pd
import numpy as np
import uuid
from datetime import datetime, timedelta

NUM_RECORDS = 10000000
CHUNK_SIZE = 1000000
OUTPUT_FILE = "large_order_data_2024_10M.csv"

BRANCHES = ['KHONKAEN', 'PHUKET', 'CHIANGMAI', 'HATYAI', 'BANGKOK']
BRANDS = ['PUMA', 'REEBOK', 'ADIDAS', 'NIKE', 'NEWBALANCE']
PRODUCT_TYPES = ['PANT', 'SHOE', 'BAG', 'SOCK']
BRAND_PREFIX_MAP = { 'PUMA': 'PU', 'REEBOK': 'RE', 'ADIDAS': 'AD', 'NIKE': 'NI', 'NEWBALANCE': 'NE' }

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31, 23, 59, 59)
time_delta_seconds = int((end_date - start_date).total_seconds())

print(f"Generating {NUM_RECORDS:,} records in chunks of {CHUNK_SIZE:,}...")

def generate_unique_order_ids(n):
    # สร้าง order_no ไม่ซ้ำกัน n ค่า ด้วย UUID 10 หลัก
    order_ids = []
    while len(order_ids) < n:
        new_id = str(uuid.uuid4().int)[0:10]
        order_ids.append(f"ORD{new_id}")
    return order_ids

for i in range(0, NUM_RECORDS, CHUNK_SIZE):
    n = min(CHUNK_SIZE, NUM_RECORDS - i)
    print(f"  ▶ Generating records {i+1:,} to {i+n:,}")

    # order_no
    order_nos = generate_unique_order_ids(n)

    # amount
    amounts = np.random.randint(500, 20001, size=n)

    # customer_no : สร้างรหัสลูกค้า CUST0001 ถึง CUST9999
    customer_pool = [f"CUST{k:04d}" for k in range(1, 10000)]
    customer_nos = np.random.choice(customer_pool, size=n)

    # branch & brand
    branches = np.random.choice(BRANCHES, size=n)
    brands = np.random.choice(BRANDS, size=n)

    # sku
    product_type_choices = np.random.choice(PRODUCT_TYPES, size=n)
    sku_numbers = np.random.randint(5, 31, size=n)
    brand_prefixes = pd.Series(brands).map(BRAND_PREFIX_MAP)
    skus = brand_prefixes + '-' + product_type_choices + '-' + pd.Series(sku_numbers).astype(str).str.zfill(2)

    # quantity
    quantities = np.random.randint(1, 6, size=n)

    # datetime
    random_seconds = np.random.randint(0, time_delta_seconds + 1, size=n)
    transaction_datetimes = [start_date + timedelta(seconds=int(s)) for s in random_seconds]

    # dataframe
    df = pd.DataFrame({
        'order_no': order_nos,
        'amount': amounts,
        'customer_no': customer_nos,
        'branch': branches,
        'brand': brands,
        'sku': skus,
        'quantity': quantities,
        'transaction_datetime': transaction_datetimes })

    # append to csv
    df.to_csv(OUTPUT_FILE, index=False, mode='a', header=(i == 0))

print(f"✅ Done! Saved to {OUTPUT_FILE}")
