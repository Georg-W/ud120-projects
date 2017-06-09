#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, precision_score

X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()

clf.fit(X_train, y_train)

pred = clf.predict(X_test)

print "pred: ", len(X_test)

print "pred: ", pred

print "recall: ", recall_score(pred, y_test)

print "precision: ", precision_score(pred, y_test)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print "recall: ", recall_score(predictions, true_labels)

print "precision: ", precision_score(predictions, true_labels)

print "new: ", y_test
print clf.score(X_test, y_test)

### your code goes here 


