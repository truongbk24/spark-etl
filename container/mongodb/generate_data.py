import random
import string
from pymongo import MongoClient
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient("mongodb://mongodb:27017/")
db = client.crm
customers_collection = db.customer
transactions_collection = db.transaction

# Function to generate a random name
def random_name():
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
    last_names = ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate a random email
def random_email(name):
    domains = ['example.com', 'mail.com', 'test.com', 'sample.com']
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{username}@{random.choice(domains)}"
# Function generate random date in a year
def random_datetime_in_august(year=2024):
    # Define the start and end of August
    start_date = datetime(year, 8, 1)
    end_date = datetime(year, 9, 1)

    # Get the total number of seconds between the start and end dates
    time_between_dates = end_date - start_date
    seconds_between_dates = time_between_dates.total_seconds()

    # Generate a random number of seconds to add to the start date
    random_seconds = random.uniform(0, seconds_between_dates)

    # Add the random seconds to the start date
    random_date = start_date + timedelta(seconds=random_seconds)
    
    return random_date

# Generate 1000 rows of data
def generate_customers():
    data = []
    for i in range(1, 1001):
        name = random_name()
        email = random_email(name)
        age = random.randint(18, 60)
        record = {"id": i, "name": name, "age": age, "email": email}
        data.append(record)
    # Insert data into the collection
    customer_ids = customers_collection.insert_many(data).inserted_ids
    return customer_ids

def generate_transaction_by_customer(customer_id):
    return {
        "customer_id": customer_id,
        "amount": round(random.uniform(10.0, 1000.0), 2),  # Random amount between 10 and 1000
        "currency": "USD",
        "transaction_date": random_datetime_in_august(),
        "description": random.choice([
            "Grocery Shopping", "Electronics Purchase", "Restaurant", "Clothing", "Fuel Purchase"
        ])
    }

def generate_transactions(customer_ids):
    transactions = []
    for customer_id in customer_ids:
        transactions.extend([generate_transaction_by_customer(customer_id) for _ in range(10)])
    # Insert all transactions at once (batch insert for efficiency)
    transactions_collection.insert_many(transactions)

customer_ids=generate_customers()
generate_transactions(customer_ids)

print("Data inserted successfully!")
