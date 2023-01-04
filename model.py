# import tools
import sklearn.preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd

import acquire as a
import prepare as pre 

###################################

def model_prep_stmt(train,validate,test):

    # keeping features columns
    keep_cols = ['senior_citizen',
                 'tenure',
                 'monthly_charges',
                 'tech_support_Yes',
                 'churn_Yes']
    
    # making new data frames with only the features above
    train = train[keep_cols]
    validate = validate[keep_cols]
    test = test[keep_cols]
    
    # Split data into predicting variables (X) and target variable (y) and reset the index for each dataframe
    # creating x and y versions of train to remove the target variable
    train_x = train.drop(columns=['churn_Yes'])
    train_y = train.churn_Yes

    # creating x and y versions of train to remove the target variable
    validate_x = validate.drop(columns=['churn_Yes'])
    validate_y = validate.churn_Yes

   # creating x and y versions of train to remove the target variable
    test_x = test.drop(columns=['churn_Yes'])
    test_y = test.churn_Yes
    
    return train_x, validate_x, test_x, train_y, validate_y, test_y

###################################

def get_tree(train_x,validate_x,train_y,validate_y,md):
    
    # create classifier object
    clf = DecisionTreeClassifier(max_depth=md, random_state=42)
    
    #fit model on training data
    clf = clf.fit(train_x, train_y)
    
    # print result
    print('Decision Tree')
    print(f"Accuracy of Decision Tree on train data is {clf.score(train_x, train_y)}")
    print(f"Accuracy of Decision Tree on validate data is {clf.score(validate_x, validate_y)}")
    
###################################

def get_forest(train_x, validate_x, train_y, validate_y,md):
    
    '''get random forest accuracy on train and validate data'''

    # create model object and fit it to training data
    rf = RandomForestClassifier(max_depth=md, random_state=123)
    rf.fit(train_x,train_y)

    # print result
    print('Random Forest')
    print(f"Accuracy of Random Forest on train is {rf.score(train_x, train_y)}")
    print(f"Accuracy of Random Forest on validate is {rf.score(validate_x, validate_y)}")
    
###################################

def get_reg(train_x, validate_x, train_y, validate_y):
    
    '''get logistic regression accuracy on train and validate data'''

    # create model object and fit it to the training data
    logit = LogisticRegression(solver='liblinear')
    logit.fit(train_x, train_y)

    # print result
    print('Logistic Regression')
    print(f"Accuracy of Logistic Regression on train is {logit.score(train_x, train_y)}")
    print(f"Accuracy of Logistic Regression on validate is {logit.score(validate_x, validate_y)}")

###################################

def get_knn(train_x, validate_x, train_y, validate_y,kn):
    
    '''get KNN accuracy on train and validate data'''

    # create model object and fit it to the training data
    knn = KNeighborsClassifier(n_neighbors=kn, weights='uniform')
    knn.fit(train_x, train_y)

    # print results
    print('KNN')
    print(f"Accuracy of KNN on train is {knn.score(train_x, train_y)}")
    print(f"Accuracy of KNN on validate is {knn.score(validate_x, validate_y)}")

###################################

def get_best_model(train_x, validate_x, train_y, validate_y,md,test_x):
    '''get random forest accuracy on train and validate data and creates dataframe
       on test set.
    '''

    # create model object and fit it to training data
    rf = RandomForestClassifier(max_depth=md, random_state=42)
    rf.fit(train_x,train_y)
    
    #prints feature importance for visual
    print("feature importance")
    print('\n')
    print(rf.feature_importances_)
    
    # creates array of predictions based on test data
    y_pred = rf.predict(test_x)
    
    # creates array of probability of each prediction based on test data
    y_pred_proba = rf.predict_proba(test_x)
    
    # creates data frame and cleans columns.
    prob_pred = pd.DataFrame(y_pred_proba,y_pred)
    prob_pred.rename(columns={0: 'Probability', 1: 'Predictions'}, inplace=True)

    prob_pred = prob_pred.reset_index(drop=True)
    

    return prob_pred
    



