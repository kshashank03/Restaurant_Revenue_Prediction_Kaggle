#%% [markdown] 
# Import Libraries
# %%
import pandas as pd
import os
# %%
pwd = os.getcwd()

# %%
train_import = pd.read_csv(pwd + "/train.csv")
train_import
# %%
# Let's take a look at the columns
train_import.columns
# %%
train_import["City"].unique()
# %%
train_import["City Group"].unique()
# %%
train_import["Type"].unique()
# FC: Food Court, IL: Inline, DT: Drive Thru, MB: Mobile
# %%
train_import["revenue"].describe()
# %%
