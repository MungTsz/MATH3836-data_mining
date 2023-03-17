import pandas as pd
import visualise as viz

train_path = 'extracted/train.csv'
test_path = 'extracted/test.csv'
df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)




# # print(df_train.head())
# '''
# Data Exploring
# plotting correlation matrix - identifying highly correlated features -> feature selection
# Data Cleaning/Manipulation - Missing Data, Outliers, Standardization
# '''
#
# print(f'{len(df_train.columns)} Columns available \n', df_train.columns)
# print('Details of each feature could be found in data_description.txt')
# viz.heatmap(df_train)
# print('corr\n',df_train.corr().SalePrice.abs().loc[lambda x:x>0.3].sort_values(ascending=False))
# # print('descending corr\n', df_train.corr().SalePrice.abs().sort_values(ascending=False))
# # upper = df_train.corr().abs().where(np.triu(np.ones(df_train.corr().abs().shape), k=1).astype(bool))
#
# print('===============================================================')
# # Try showing the corr() after one-hot
#
#
# df_train_onehot = pd.get_dummies(df_train)
# viz.heatmap(df_train_onehot)
# print('corr\n',df_train_onehot.corr().SalePrice.abs().loc[lambda x:x>0.3].sort_values(ascending=False))
# # print('descending corr\n', df_train_onehot.corr().SalePrice.abs().sort_values(ascending=False))
#
# # df_train_onehot = pd.get_dummies(df_train, columns=df_train.loc[:, df_train.dtypes == object].columns)
# # df_train_onehot = pd.concat([df_train_onehot, df_train.SalePrice], axis=1)
# # print(df_train_onehot.corr().SalePrice.abs().iloc[:,0].sort_values(ascending=False))
#
# # viz.heatmap(df_train_onehot)
#
#
# # print(df_train_onehot.corr().SalePrice.abs().loc[lambda x:x>0.3].sort_values(ascending=False))
# '''
# OverallQual: Rates the overall material and finish of the house. However we don't know the standards of rating
# GrLivArea: Above grade (ground) living area square feet
# GarageCars: Size of garage in car capacity
# # GarageArea: Size of garage in square feet (Remove this, GarageCars is good enough)
# TotalBsmtSF: Total square feet of basement area
# YearBuilt: Original construction date
# '''
#
#
# viz.box_plot(df_train_onehot, 'OverallQual', 'SalePrice')
# viz.scatter_plot(df_train_onehot, 'GrLivArea', 'SalePrice')
# viz.box_plot(df_train_onehot, 'GarageCars', 'SalePrice')
# viz.scatter_plot(df_train_onehot, 'TotalBsmtSF', 'SalePrice')
# viz.scatter_plot(df_train_onehot, 'YearBuilt', 'SalePrice')
# viz.scatter_plot(df_train_onehot, 'YrSold', 'YearBuilt')



# Check null values
print(df_train.isnull().sum().loc[lambda x:x>0].sort_values(ascending=False))

'''
PoolQC          NA = No Pool
MiscFeature     NA = No Miscellaneous feature
Alley           NA = No alley access
Fence           NA = No Fence
FireplaceQu     NA = No Fireplace
LotFrontage      259
GarageType      Can remove column
GarageYrBlt     Can remove column
GarageFinish    Can remove column
GarageQual      Can remove column
GarageCond      Can remove column
BsmtExposure    Can remove column
BsmtFinType2    Can remove column
BsmtFinType1    Can remove column
BsmtCond        Can remove column
BsmtQual        Can remove column
MasVnrArea      Can remove column
MasVnrType      Can remove column
Electrical      drop NA
'''
