import csv
import sys
import numpy as np
from Helper_Functions import *

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import *

X_reg_list = []
Y_reg_list = []
actual_data = np.array([])

print "Preprocessing..."

with open('Salaries.csv', 'rb') as csvfile:
    csv = csv.DictReader(csvfile, delimiter=',')

    Header_skipped = False
    count = 0
    for row in csv:
        count += 1

        # skip the first line in csv file. contains header.
        if not Header_skipped: Header_skipped = True; continue;
        if row['JobTitle'] == 'Not provided': continue;

        job_title = row['JobTitle'].lower()
        year = float(row['Year'])
        total_pay = total_pay_converter(inflation(float(row['TotalPayBenefits']), year))
        if total_pay <= 0:
            continue;
        status = row['Status']
        if status == '' or status == None:
            status = 'uk'
        #status = status_calc(row['Status'], total_pay).lower()

        X_reg_list.append([job_title, status])
        Y_reg_list.append([total_pay])

        #actual_data = append_to_array(actual_data, [job_title, status, total_pay])

        #sys.stdout.flush()
        #if count > : break

print "converting to np array..."
X = np.array(X_reg_list)
Y = np.array(Y_reg_list)

labler_job = preprocessing.LabelEncoder()
labler_status = preprocessing.LabelEncoder()

X1 = labler_job.fit_transform(X[:, 0])
X1I = labler_job.inverse_transform(X1)

X2 = labler_status.fit_transform(X[:, 1])
X2I = labler_status.inverse_transform(X2)
print "unique jobs: ", str(unique_jobs_count(X))

X_train = np.array(zip(X1, X2, Y))

methods = [LinearRegression(), BayesianRidge()]#, svm.SVR(), Ridge(), Lasso()]

to_predict = ["account clerk","ft"]
prediction1 = encode_prediction(to_predict, X1, X1I, X2, X2I)
to_predict = ["account clerk","pt"]
prediction2 = encode_prediction(to_predict, X1, X1I, X2, X2I)
to_predict = ["GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY","ft"]
prediction3 = encode_prediction(to_predict, X1, X1I, X2, X2I)

for method in methods:
    searchCV = method
    print "Fitting..."
    searchCV.fit(X_train, Y)

    print
    print
    #print "sal for: " + str(prediction1)
    #print "Pred:    " + str(searchCV.predict(prediction1))
    #print "sal for: " + str(prediction2)
    #print "Pred:    " + str(searchCV.predict(prediction2))
    #print "sal for: " + str(prediction3)
    #print "Pred:    " + str(searchCV.predict(prediction3))
    print "SCORE:   " + str(searchCV.score(X_train, Y))
    #print "Pred:   " + str(searchCV.predict(X_train[200]))
    #exit()

    print searchCV.coef_
    #print str(cross_val_score(searchCV, X_train, Y, scoring="neg_mean_absolute_error"))
    print str(cross_val_score(searchCV, X_train, Y, scoring="neg_mean_squared_error"))

plt.plot([x for x, y, z in zip(X1, X2, Y) if y==0], [z for x, y, z in zip(X1, X2, Y) if y==0], 'ro')
plt.plot([x for x, y, z in zip(X1, X2, Y) if y==1], [z for x, y, z in zip(X1, X2, Y) if y==1], 'b.')
#plt.plot([x for x, y, z in zip(X1, X2, Y) if y==2], [z for x, y, z in zip(X1, X2, Y) if y==2], 'g.')
plt.show()
