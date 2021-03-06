# -*- coding: utf-8 -*-
"""bostonHousePricePrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nfp61c3iw2Njevm_TOJUVohQUi7lsKOM
"""

import numpy as np
import matplotlib.pyplot as plt 

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.ensemble import AdaBoostRegressor
from sklearn import metrics
from sklearn.datasets import load_boston
from sklearn import datasets
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer

def load_data():
    boston = datasets.load_boston()
    return boston

def performance_metric(label, prediction):
    return r2_score(label,prediction)
    pass


def split_data(city_data):
    X, y = city_data.data, city_data.target
    X_train, X_test, y_train, y_test = train_test_split(
         X, y, test_size=0.30, random_state=1)
    return X_train, y_train, X_test, y_test


  
def fit_predict_decisiontree_model(city_data):
    regressor = DecisionTreeRegressor(random_state=1)

    parameters = {'max_depth':(None,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),
                  'max_features':(None,1,2,3,13),
        'min_samples_split': (2,3,4,5,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,27,100),
        'min_samples_leaf': (1, 2, 3)
    }

    X_train, y_train, X_test, y_test = split_data(city_data)

    scoring_fnc = make_scorer(performance_metric)
    regressors = GridSearchCV(regressor, parameters, scoring=scoring_fnc)
    regressors.fit(X_train,y_train)
    reg = regressors.best_estimator_
    print(reg)

    #reg = DecisionTreeRegressor(max_depth=40, max_features=None, min_samples_split=50, min_samples_leaf=50, random_state=1)

    reg.fit(X_train, y_train)
    y_dtreePred=reg.predict(X_test)
    dtreeMSE = mean_squared_error(y_test,y_dtreePred)
    print("MSE      = " + str(dtreeMSE))
    
    
def fit_predict_model_adaboost(city_data):
    regressor = AdaBoostRegressor(DecisionTreeRegressor(),random_state=1)
    
    parameters = {'n_estimators':(5,10,20,50,80,95,100),
                  'learning_rate' : (0.001,0.01,0.1,1.0)
    }

    X_train, y_train, X_test, y_test = split_data(city_data)

    scoring_fnc = make_scorer(performance_metric)
    regressors = GridSearchCV(regressor, parameters, scoring=scoring_fnc)

    regressors.fit(X_train,y_train)

    reg = regressors.best_estimator_
    print(reg)

    #reg = AdaBoostRegressor(n_estimators = 1000, learning_rate = 0.01)
    reg.fit(X_train, y_train)
    
    y_dtreePred=reg.predict(X_test)

    dtreeMSE = mean_squared_error(y_test,y_dtreePred)
    print("MSE      = " + str(dtreeMSE))
    
def main():
    city_data = load_data()
    fit_predict_decisiontree_model(city_data)
    fit_predict_model_adaboost(city_data)

if __name__ == "__main__":
    main()