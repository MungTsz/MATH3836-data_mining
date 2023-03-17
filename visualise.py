import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def heatmap(dataset):
    plt.figure(figsize=(10, 8))
    sns.heatmap(dataset.corr(), cmap='coolwarm', square=True)
    _ = plt.title('Correlation Matrix')
    plt.show()
def box_plot(dataset,x,y):
    plt.figure(figsize=(10, 8))
    df = pd.concat([dataset[y],dataset[x]],axis=1)
    sns.boxplot(x=x,y=y,data=df)
    _ = plt.title(f'{x} vs {y}')
    plt.show()
def scatter_plot(dataset,x,y):
    plt.figure(figsize=(10, 8))
    df = pd.concat([dataset[y], dataset[x]], axis=1)
    sns.scatterplot(x=x, y=y, data=df)
    _ = plt.title(f'{x} vs {y}')
    plt.show()
