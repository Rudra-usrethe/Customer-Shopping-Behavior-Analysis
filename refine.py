import pandas as pd 
df = pd.read_csv("customer_shopping_behavior.csv")
# print(df.head())
# print(df.info())
# print(df.describe(include="all")) 
# print(df.isnull().sum())   # to see which columns have null value .sum() give total number of null values 
# df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(lambda x:x.fillna(x.median()))
# print(df.isnull().sum())

# now converting columns names into lower case for more felexbity 
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ","_")
# print(df.columns)
df= df.rename(columns={"purchase_amount_(usd)":"purchase_amount"})
# print(df.columns)
labels =["Young Adult" , "Adult","Middle-age","senior"]
df["age_group"]=pd.qcut(df["age"], q=4 , labels=labels)
# print(df[["age","age_group"]].head(5))
frequency_mapping={"Fortnight":14,"Weekly":7,"Monthly":30,"Quarterly":90,"Bi-Weekly":90,"Annually":365,"Every 3 Months":90}
df["purchase_frequency_days"]=df["frequency_of_purchases"].map(frequency_mapping)
# print(df[["purchase_frequency_days","frequency_of_purchases"]].head(10))
# df = df.drop("promo_code_used",axis=1) # promo_code_used and discount applied have same data so its only increases the data 
# print(df.columns)



# connect sql
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = quote_plus("18@r")
host = "localhost"
port = "3306"
database = "project_data_analyist"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

table_name = "mytable"

df.to_sql(table_name, engine, if_exists="replace", index=False)

result = pd.read_sql("SELECT * FROM mytable LIMIT 5;", engine)

print(result)