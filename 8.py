from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ElectricityBillingSystem"]
collection = db["electricity_bills"]

name = input("Enter Customer Name: ")
consumer_id = input("Enter Consumer ID: ")
units = float(input("Enter units consumed (kWh): "))

rate_per_unit = 1.5
total_bill = units * rate_per_unit

bill_data = {
    "Customer Name": name,
    "Consumer ID": consumer_id,
    "Units Consumed": units,
    "Rate per Unit": rate_per_unit,
    "Total Bill": total_bill
}

collection.insert_one(bill_data)

print("\nBill Generated Successfully!")
print("---------------------------------")
print(f"Customer Name  : {name}")
print(f"Consumer ID    : {consumer_id}")
print(f"Units Consumed : {units} kWh")
print(f"Rate per Unit  : ₹{rate_per_unit}")
print(f"Total Bill     : ₹{total_bill}")
print("---------------------------------")