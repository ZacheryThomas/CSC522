import csv
import sys
import numpy as np
from Helper_Functions import *

import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn import svm
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import *

X = np.array([])
Y = np.array([])
actual_data = np.array([])
with open('Salaries_AC.csv', 'rb') as csvfile:
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
        status = status_calc(row[12], total_pay)
        if status == "PT": continue

        X = append_to_array(X, [job_title, status])
        Y = append_to_array(Y, total_pay)
        actual_data = append_to_array(actual_data, [job_title, status, total_pay])
        count += 1
        #sys.stdout.write("\r" + str(float(count)))
        #sys.stdout.write("\r" + str(float(count)/150000 * 100))
        #sys.stdout.flush()
        #if count > 30000: break

labler_job = preprocessing.LabelEncoder()
labler_status = preprocessing.LabelEncoder()

X1 = labler_job.fit_transform(X[:, 0])
X1I = labler_job.inverse_transform(X1)


temp1 = []
temp2 = []
for x in actual_data:
    if x[0] == "account clerk":
        print x
        temp1.append(0)
        temp2.append(x[2])


sum = 0
count = 0
temp = []

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

for x in range(len(actual_data)):
    if actual_data[x][1] == "FT":
        sum += float(actual_data[x][2])
        temp.append(actual_data[x][2])
        count += 1
print "median of FT: " + str(median(temp))
print count
print sum
print "avg " + str(sum / count)

#plt.plot(temp1, temp2, 'ro')
#plt.show()

X2 = labler_status.fit_transform(X[:, 1])
X2I = labler_status.inverse_transform(X2)
print "\nunique jobs: ", str(unique_jobs_count(X))
#X_train = np.array([X1[0], X2[0], X3[0]])#, np.float64)

#plt.plot(X1, Y, 'ro')
#plt.show()

X_train = np.array([])
for x1_val, x2_val in zip(X1, X2):
    X_train = append_to_array(X_train, [x1_val, x2_val])


methods = [LinearRegression(), BayesianRidge(), svm.SVR(), Ridge(), Lasso()]


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
    print X[0]
    print "Actual: " + str(Y[0])
    print "Pred:   " + str(searchCV.predict(X_train[200]))
    #exit()

    print "\n" + str(method) + "\n" + str(cross_val_score(searchCV, X_train, Y))

