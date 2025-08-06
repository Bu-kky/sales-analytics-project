import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("9. Sales-Data-Analysis.csv")
df["Manager"]=df["Manager"].str.strip().str.replace(" ","") #removes extra spaces to make sure no name is duplicated in the result
print(df.head())
print(df.info())

print(df["City"].value_counts()) #Shows the cities and their performances
print(plt.hist(df["City"])) #displays a histogram to visualize the city performance
print(plt.title("City analysis"))

print(df.groupby("Product")["Quantity"].sum()) #Shows the total quantity of each of the products bought
print(df["Product"].value_counts()) #shows the number of times a product is bought

print(df["Purchase Type"].value_counts()) #shows the number of times each purchase type is used

print(df["Manager"].value_counts()) #shows the number of times each manager makes a sale
print(df.groupby("Manager")["Quantity"].sum()) #shows the total quantity sold by each manager
print(plt.hist(df["Manager"])) #displays a histogram to visualize manager performance
print(plt.title("Manager performance analysis"))

df["Total Profit"]= df["Price"] * df["Quantity"] #adds a new column named Total profit
print(df) #displays new table
print(df.groupby("Manager")["Total Profit"].sum()) #displays the total amoun earned by each manager
