#!/usr/bin/env python

""" K-nearest neighbor classifier """

__author__ = ['@mgiles717']
__all__ = ["KNNClassifier"]

import numpy as np
import pandas as pd

#from datasets.load_datasets import load_migraine

class KNNClassifier():
    """
    KNN Classifier
    
    Manual implementation of the KNN algorithm.
    
    Parameters
    ----------
    n_neighbors : int, optional (default=5)
    
    """
    
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors
        
    def train(self, data, labels):
        pass
    
    def predict(self, predict):
        pass


if __name__ == "__main__":
    print("Hello")