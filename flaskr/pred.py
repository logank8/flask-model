import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

## How to connect the model:
## At the start of each new session, retrain the model and create one instance of an object that can take arguments
##  and spit out a prediction



# Function to make predictions 
def prediction(X_test, clf_object):
    # Predicton on test with giniIndex 
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred) 
    return y_pred


# Function to calculate accuracy 
def cal_accuracy(y_test, y_pred):
    print ("Accuracy : ", accuracy_score(y_test,y_pred)*100) 


def __init__():
    song_data = pd.read_csv("song_data.csv")
    df = pd.DataFrame(song_data)
    X = song_data[['instrumentalness', 'energy', 'loudness', 'danceability']]
    Y = song_data.song_popularity

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)


    # perform training with giniIndex
    # Creating the classifier object 
    clf_gini = DecisionTreeClassifier(criterion = "gini",random_state = 100,max_depth=25, min_samples_leaf=5)
    # Fit the model 
    clf_gini.fit(X_train, y_train) 

    # perform training with entropy
    # Decision tree with entropy 
    clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,max_depth = 25, min_samples_leaf = 5)
    # Fit the model  
    clf_entropy.fit(X_train, y_train) 

    # Operational Phase 
    print("Results Using Gini Index:")
    # Prediction using gini 
    y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)

    print("Results Using Entropy:")
    # Prediction using entropy 
    y_pred_entropy = prediction(X_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy) 

    