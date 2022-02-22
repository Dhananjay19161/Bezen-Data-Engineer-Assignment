# %%
import pandas as pd

# %%
df=pd.read_csv('2022_02_08-02_30_31_AM.csv')

# %%
df.info()

# %%
df.head()

# %%
#Query 1 Product without prices
Product_without_prices = df.loc[df['price_string'].isnull()]

# %%
Product_without_prices

# %%
Product_with_prices=df.loc[df['price_string'].notnull()]

# %%
Product_with_prices

# %%
#Count of products without prices in Each Product Type,Category,Level1
df1=Product_without_prices.groupby(['product_type','category','level_1']).size().reset_index(name='count')

# %%
df1

# %%
#Count of products without prices in Each Product Type,Category,Level1
df2=Product_with_prices.groupby(['product_type','category','level_1']).size().reset_index(name='count')

# %%
df2

# %%
Product_with_prices.reset_index(inplace=True)

# %%
Product_with_prices['price_string'] = Product_with_prices['price_string'].str.replace('$', '')

# %%
Product_with_prices['price_string']

# %%
Product_with_prices.insert(2, "currency", "$")

# %%
Product_with_prices

# %%
Product_with_prices.rename(columns = {'price_string':'value'}, inplace = True)

# %%
Product_with_prices

# %%
Product_with_prices['value']=Product_with_prices['value'].astype(float)

# %%
category_wise=Product_with_prices.groupby('category')['value'].mean()

# %%
category_wise


