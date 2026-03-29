import pandas as pd

#load data
sales_data = pd.read_csv(r'C:\Users\shobi\Documents\GitHub\Sales-Data-Analysis\sales_data.csv')

#preview data
print(sales_data.head(10))

#shape
print("Shape :",sales_data.shape)

#describe
print(sales_data.describe())

#columns
print("Columns :",sales_data.columns)

#Datatypes
print(sales_data.dtypes)

#info
print(sales_data.info())

#Unique values
print("Product :" ,sales_data["Product"].unique())
print("Region :" ,sales_data["Region"].unique())

#Cleaning data
print(sales_data.isnull().sum())
print(sales_data.duplicated().sum())

#convert date
sales_data["Date"] = pd.to_datetime(sales_data["Date"])
print(sales_data["Date"].head(10))

#month wise sales
sales_data["Month"] = sales_data["Date"].dt.month_name()
print(sales_data["Month"].unique())
Month_sales = sales_data.groupby("Month")["Total_Sales"].sum().sort_index(ascending=False)
print("Month wise sales :", Month_sales )
Top_Month = Month_sales.head(1)
Least_Month = Month_sales.tail(1)

#Analysis data
Total_Revenue = sales_data["Total_Sales"].sum()
print("Total revenue :",Total_Revenue)
Total_Quantity = sales_data["Quantity"].sum()
print("Total quantity :" ,Total_Quantity)

#find the best
Best_Products = sales_data.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
print(Best_Products)
top_product = Best_Products.head(1)
least_product = Best_Products.tail(1)

#Region wise sale
Region_Sales = sales_data.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
print(Region_Sales)
Top_Region = Region_Sales.head(1)
Least_Region = Region_Sales.tail(1)

#Customer wise sale
Best_Customer = sales_data.groupby("Customer_ID")["Total_Sales"].sum().sort_values(ascending=False)
print(Best_Customer.head(10))
Top_Customer  = Best_Customer.head(1)
Least_Customer  = Best_Customer.tail(1)

#profitable products
Profitable_Products = sales_data.groupby("Product")["Total_Sales"].sum().idxmax()
print("Profitable products :",Profitable_Products)

#Highest sales day
Best_Day = sales_data.groupby("Date")["Total_Sales"].sum().sort_values(ascending=False)
print("Best day on sale :",Best_Day.head(10))
Top_Day = Best_Day.head(1)
Least_Day = Best_Day.tail(1)

#Most sold products Quantity
top_quantity = sales_data.groupby("Product")["Quantity"].sum().idxmax()
print("Top quantity product :", top_quantity)

#Average Order value
Average_order = sales_data["Total_Sales"].mean()
print(Average_order)

#Create report
print("\n---Sales Report---")
print(f"Total revenue : ₹{Total_Revenue:,.2f}")

print(f"Total quantity : ₹{Total_Quantity:,.2f}")

print("\nTop Products :")
for Product, Total_Sales in top_product.items():
    print(f"{Product} :  ₹{Total_Sales} ")

print("\nLeast Products :")
for Product, Total_Sales in least_product.items():
    print(f"{Product} :  ₹{Total_Sales} ")

print("\nTop Customer :")
for Customer_ID, Total_Sales in Top_Customer.items():
    print(f"{Customer_ID} : ₹{Total_Sales}")

print("\nLeast Customer :")
for Customer_ID, Total_Sales in Least_Customer.items():
    print(f"{Customer_ID} : ₹{Total_Sales}")

print("\nTop Sales by Region :")
for Region, Total_Sales in Top_Region.items():
    print(f"{Region} : ₹{Total_Sales} ")

print("\nLeast Sales by Region :")
for Region, Total_Sales in Least_Region.items():
    print(f"{Region} : ₹{Total_Sales} ")

print("\nTop sale on Day :")
for Date, Total_Sales in Top_Day.items():
    print(f"{Date} : ₹{Total_Sales}")

print("\nLeast sale on Day :")
for Date, Total_Sales in Least_Day.items():
    print(f"{Date} : ₹{Total_Sales}")

print("\nTop sale on Month :")
for Month, Total_Sales in Top_Month.items():
    print(f"{Month} : ₹{Total_Sales}")
    
print("\nLeast sale on Month :")
for Month, Total_Sales in Least_Month.items():
    print(f"{Month} : ₹{Total_Sales}")
