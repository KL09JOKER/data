from pymongo import MongoClient
from tabulate import tabulate

client=MongoClient("mongodb://localhost:27017/")
db=client["librarydb"]
b=db["book"]
books=list(b.find({},{"_id":0}))
print(tabulate(books,headers="keys",tablefmt="grid"))