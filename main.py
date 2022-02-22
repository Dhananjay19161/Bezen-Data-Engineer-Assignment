# %% [markdown]
# # Importing Libraries

# %%
import pandas as pd

# %% [markdown]
# # Reading csv file

# %%
df=pd.read_csv('2022_02_08-02_30_31_AM.csv')

# %%
df.info()

# %%
df.head()

# %% [markdown]
# # Query 1=> Product without Prices

# %%
#Query 1 Product without prices
Product_without_prices = df.loc[df['price_string'].isnull()]

# %%
Product_without_prices

# %% [markdown]
# # Product with Prices

# %%
Product_with_prices=df.loc[df['price_string'].notnull()]

# %%
Product_with_prices

# %% [markdown]
# # Query 2=>

# %% [markdown]
# ## Count of products without prices in Each Product Type,Category,Level1

# %%
#Count of products without prices in Each Product Type,Category,Level1
count_product_without_prices=Product_without_prices.groupby(['product_type','category','level_1']).size().reset_index(name='count of products')

# %%
count_product_without_prices

# %% [markdown]
# ## Count of products with prices in Each Product Type,Category,Level1

# %%
#Count of products without prices in Each Product Type,Category,Level1
count_product_with_prices=Product_with_prices.groupby(['product_type','category','level_1']).size().reset_index(name='count of products')

# %%
count_product_with_prices

# %% [markdown]
# # Query 3=>

# %% [markdown]
# ## Removing $ from price string so as to make it numeric

# %%
Product_with_prices['price_string'] = Product_with_prices['price_string'].str.replace('$', '')

# %% [markdown]
# ## Again Inserting $ to make all prices with dollar

# %%
Product_with_prices['price_string'] ='$'+ Product_with_prices['price_string'].astype(str)

# %%
Product_with_prices['price_string']

# %% [markdown]
# ## Creating new field value extracted from price_string and saved as float

# %%
value=Product_with_prices['price_string'].str.replace('$', '').astype(float)

# %%
value

# %% [markdown]
# ## Inserting a currency column and value column

# %%
Product_with_prices.insert(2, "currency", "$")

# %%
Product_with_prices.insert(3, "value", value)

# %%
Product_with_prices

# %% [markdown]
# ## Query 4 =>

# %%
category_wise=Product_with_prices.groupby('category')['value'].mean().reset_index(name='Average Price')

# %%
category_wise


