# %% [markdown]
# # Importing Libraries

# %%
import pandas as pd
import seaborn as sns

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
count_product_without_prices_product_type=Product_without_prices.groupby(['product_type']).size().reset_index(name='count of products')

# %%
count_product_without_prices_category=Product_without_prices.groupby(['category']).size().reset_index(name='count of products')
count_product_without_prices_level_1=Product_without_prices.groupby(['level_1']).size().reset_index(name='count of products')



# %%
count_product_without_prices_product_type

# %%
count_product_without_prices_category

# %%
count_product_without_prices_level_1

# %% [markdown]
# ## Count of products with prices in Each Product Type,Category,Level1

# %%
#Count of products without prices in Each Product Type,Category,Level1
count_product_with_prices_product_type=Product_with_prices.groupby(['product_type']).size().reset_index(name='count of products')
count_product_with_prices_category=Product_with_prices.groupby(['category']).size().reset_index(name='count of products')
count_product_with_prices_level_1=Product_with_prices.groupby(['level_1']).size().reset_index(name='count of products')

# %%
count_product_with_prices_product_type

# %%
count_product_without_prices_category

# %%
count_product_with_prices_level_1

# %% [markdown]
# # Query 3=>

# %% [markdown]
# ## Removing $ from price string so as to make it numeric

# %%
Product_with_prices['price_string'] = Product_with_prices['price_string'].str.replace('$', '')

# %% [markdown]
# ## Fixing Unfiltered Prices

# %%
unfiltered=df.loc[df['price_string_unf'].notnull()]


# %%
unfiltered

# %% [markdown]
# ## Removed alphabets from price_string_unf

# %%
unfiltered['price_string_unf'] = unfiltered['price_string_unf'].str.replace("[a-zA-Z]", '')


# %% [markdown]
# ## Removed : from price_string_unf

# %%
unfiltered['price_string_unf'] = unfiltered['price_string_unf'].str.replace(":", '')

# %% [markdown]
# ## removed \n from price_string_unf

# %%
unfiltered['price_string_unf'] = unfiltered['price_string_unf'].str.replace('\n','')

# %% [markdown]
# ## Removed spaces from price_string_unf

# %%
unfiltered['price_string_unf'] = unfiltered['price_string_unf'].str.replace(' ','')

# %%
unfiltered['price_string_unf']

# %% [markdown]
# ## Split to remove garbage value

# %%
list=unfiltered['price_string_unf'].str.split('$',2)

# %%
x=list.apply(lambda col: col[1])

# %%
unfiltered['price_string_unf']=x

# %%
unfiltered['price_string_unf']

# %%
unfiltered['price_string_unf']='$'+ unfiltered['price_string_unf'].astype(str)

# %%
unfiltered['price_string_unf']

# %%
unfiltered

# %%
value=unfiltered['price_string_unf'].str.replace('$', '').astype(float)

# %%
value

# %%
## Therefore able to remove garbage values from price_string_unf
unfiltered.insert(3, "currency", "$")
unfiltered.insert(4, "value", value)

# %%
unfiltered

# %% [markdown]
# ## Therefore able to remove garbage values from price_string_unf

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

# %% [markdown]
# # Plots

# %% [markdown]
# ## Plotting count of products without prices for each product_type,category,level_1

# %%
sns.catplot(x="product_type", y="count of products", data=count_product_without_prices_product_type)

# %%
sns.catplot(x="category", y="count of products", data=count_product_without_prices_category)

# %%
sns.catplot(x="level_1", y="count of products", data=count_product_without_prices_level_1)

# %% [markdown]
# ## Plotting count of products with prices for each product_type,category,level_1

# %%
sns.catplot(x="product_type", y="count of products", data=count_product_with_prices_product_type)

# %%
sns.catplot(x="category", y="count of products", data=count_product_with_prices_category)

# %%
sns.catplot(x="level_1", y="count of products", data=count_product_with_prices_level_1)

# %% [markdown]
# ## Plotting category wise Average Price

# %%
sns.catplot(x="category", y="Average Price", data=category_wise)


