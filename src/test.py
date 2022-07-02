import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from models.supervised.classification.knn import KNNClassifier
from datasets.load_datasets import load_migraine

def display(data):
    plt.figure(figsize=(20,8))
    sns.heatmap(data.corr(), annot=True)
    plt.plot()
    plt.show()

if __name__ == "__main__":
    knn = KNNClassifier()
    data = load_migraine()
    
    data = data.drop(['Type'], axis=1)
    #display(data)
    df = data[['Tinnitus', 'Vertigo']]
    df['Both'] = (df['Tinnitus'] == 1) & (df['Vertigo'] == 1)
    print(df['Both'].value_counts())
    
    
    
    
    # Validation set at 10% training data
    #train_data = data.sample(frac=0.8, random_state=42)
    #test_data = data.drop(train_data.index)
    #print(train_data)
    
    
    
    