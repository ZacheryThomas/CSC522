import numpy as np

def unique_jobs_count(jobs):
    job_dict=dict()
    for x in jobs:
        job_dict[x[0]] = ''
    return len(job_dict)

def inflation(value, year):
    inflation = 1
    if year == 2011: inflation = 1.07;
    if year == 2012: inflation = 1.05;
    if year == 2013: inflation = 1.04;
    if year == 2014: inflation = 1.02;
    return inflation * value

def append_to_array(arr1, arr2):
    """
    Append two np arrays together
    if arr1 is empty, set arr1 to arr2
    :param arr1: array 1
    :param arr2: array 2
    :return:
    """
    if arr1.size == 0:
        arr1 = np.array([arr2])
        return arr1

    arr1 = np.vstack((arr1, np.array([arr2])))
    return arr1

def status_calc(status, pay):
    if status == "" or status == None:
        return ("pt" if pay < 50000 else "ft")
    return status

def total_pay_converter(pay):
    if pay < 100: return pay * 40 * 52
    elif pay < 1000: return pay * 26
    return pay

def encode_prediction(val, X1enc, X1dec, X2enc, X2dec):
    job = ''
    status = ''
    for x in range(len(X1dec)):
        if val[0].lower() == X1dec[x]:
            job = X1enc[x]
        if val[1].lower() == X2dec[x]:
            status = X2enc[x]
    if job == '': job = max(X1enc) + 1
    if status == '': status = max(X2enc) + 1
    return [job, status]

"""
PROBABLY JUNK

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
    if actual_data[x][1] == "ft":
        sum += float(actual_data[x][2])
        temp.append(actual_data[x][2])
        count += 1
print "median of FT: " + str(median(temp))
print count
print sum
print "avg " + str(sum / count)

#plt.plot(temp1, temp2, 'ro')
#plt.show()
"""