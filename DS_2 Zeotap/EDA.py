import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
def load_data():
    customers = pd.read_csv("Customers.csv")
    products = pd.read_csv("Products.csv")
    transactions = pd.read_csv("Transactions.csv")
    return customers, products, transactions

# Data Cleaning
def clean_data(customers, products, transactions):
    # Convert date columns to datetime
    customers["SignupDate"] = pd.to_datetime(customers["SignupDate"])
    transactions["TransactionDate"] = pd.to_datetime(transactions["TransactionDate"])

    # Check for and handle missing values
    customers.fillna("Unknown", inplace=True)
    products.fillna("Unknown", inplace=True)
    transactions.fillna(0, inplace=True)

    return customers, products, transactions

# EDA Functions
def explore_customers(customers):
    print("Customer Data Overview:")
    print(customers.info())
    print(customers.describe(include='all'))
    print(customers["Region"].value_counts())
    
    plt.figure(figsize=(8, 5))
    sns.countplot(data=customers, x="Region", order=customers["Region"].value_counts().index)
    plt.title("Customer Distribution by Region")
    plt.xticks(rotation=45)
    plt.show()

def explore_products(products):
    print("Product Data Overview:")
    print(products.info())
    print(products.describe(include='all'))
    print(products["Category"].value_counts())
    
    plt.figure(figsize=(8, 5))
    sns.countplot(data=products, x="Category", order=products["Category"].value_counts().index)
    plt.title("Product Distribution by Category")
    plt.xticks(rotation=45)
    plt.show()

def explore_transactions(transactions):
    print("Transaction Data Overview:")
    print(transactions.info())
    print(transactions.describe())
    
    # Temporal Analysis
    transactions["MonthYear"] = transactions["TransactionDate"].dt.to_period("M")
    monthly_sales = transactions.groupby("MonthYear")["TotalValue"].sum().reset_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_sales, x="MonthYear", y="TotalValue")
    plt.title("Monthly Sales Trend")
    plt.xticks(rotation=45)
    plt.show()

    # Top Products
    top_products = transactions.groupby("ProductID")["TotalValue"].sum().sort_values(ascending=False).head(10)
    print("Top 10 Products by Sales:")
    print(top_products)

# Main Execution
# Run each section separately in Jupyter Notebook for better interactivity
# Load data
customers, products, transactions = load_data()

# Clean data
customers, products, transactions = clean_data(customers, products, transactions)

# Explore Customers
print("\n--- Exploring Customers ---\n")
explore_customers(customers)

# Explore Products
print("\n--- Exploring Products ---\n")
explore_products(products)

# Explore Transactions
print("\n--- Exploring Transactions ---\n")
explore_transactions(transactions)
