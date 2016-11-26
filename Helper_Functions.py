import numpy as np

def inflation(value, year):
    inflation = 0
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

def total_pay_converter(pay):
    if pay < 100: return pay * 40 * 52
    elif pay < 1000: return pay * 26
    return pay
