#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print(len(features_train))
print(len(features_train[0]))

#########################################################
### your code goes here ###
from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf.fit(features_train,labels_train)
print "Training time:", round(time()-t0, 3), "s"

t0 = time()
labels_predicted = clf.predict(features_test)
print "Predicting time:", round(time()-t0, 3), "s"

acc = accuracy_score(labels_test,labels_predicted)
print(acc)
#########################################################

#For percentile = 10 and min_samples_split=40
# 15820
# 3785
# Training time: 60.707 s
# Predicting time: 0.013 s
# 0.976678043231

#When percentile = 1 and min_samples_split=40
# 15820
# 379
# Training time: 3.561 s
# Predicting time: 0.002 s
# 0.967007963595
