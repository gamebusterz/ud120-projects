#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='rbf',C=1000000)
# for rbf kernel, C = 1000000 gave an accuracy of 0.9948

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
"""
    For 1% data
    training time: 0.137 s
    prediction time: 0.989 s
    Accuracy=0.884527872582
"""
"""
    For complete data
    training time: 163.856 s
    prediction time: 17.397 s
    Accuracy = 0.984072810011
"""
t0 = time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
predicted = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"

acc = accuracy_score(labels_test,predicted)
print(acc)
#########################################################
