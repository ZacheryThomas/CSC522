import csv
import sys
import numpy as np
from Helper_Functions import *

from sklearn import preprocessing
from sklearn import svm
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression, BayesianRidge, LogisticRegressionCV, LogisticRegression

X = np.array([])
Y = np.array([])
with open('Salaries.csv', 'rb') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')

    Header_skipped = False
    count = 0
    for row in csv:
        # skip the first line in csv file. contains header.
        if not Header_skipped: Header_skipped = True; continue;
        if row[9] == 0 or row[8] == 0 or row[2] == 'Not provided': continue;

        job_title = row[2].lower()
        year = float(row[9])
        total_pay = total_pay_converter(inflation(float(row[8]), year))

        X = append_to_array(X, job_title)
        Y = append_to_array(Y, total_pay)

        count += 1
        #sys.stdout.write("\r" + str(float(count)))
        sys.stdout.write("\r" + str(float(count)/150000 * 100))
        sys.stdout.flush()
        #if count > 50000: break

labler_job = preprocessing.LabelEncoder()
X1 = labler_job.fit_transform(X[:, 0])
X1I = labler_job.inverse_transform(X1)

#X_train = np.array([X1[0], X2[0], X3[0]])#, np.float64)

X_train = np.array([])
for x_val in X1:
    X_train = append_to_array(X_train, x_val)


methods = [LinearRegression(), BayesianRidge(), svm.SVR(), svm.LinearSVR()]

print; print; print;

for method in methods:
    searchCV = method
    searchCV.fit(X_train, Y)

    #kf = KFold(n_splits=2)
    #for train, test in kf.split(X_train):
    #    X_train_jr, X_test, y_train, y_test = X[train], X[test], Y[train], Y[test]
    #    searchCV.fit(X_train, Y)

    print
    print
    print X[50000]
    print "Actual: " + str(Y[50000])
    print "Pred:   " + str(searchCV.predict(X_train[50000]))
    #exit()

    #print "\n" + str(method) + "\n" + str(cross_val_score(searchCV, X_train, Y))