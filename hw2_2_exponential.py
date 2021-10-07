import pandas as pd
import math
import numpy as np

def laplaceNoise(x,GS,epsilon):
    b = GS/epsilon
    if x<0:
        x = -x
    return math.exp(-x/b)/(2*b)

def resultWithNoise():
    data = pd.read_csv('adult.data', sep=', ', header=None, engine='python')
    colEdu = 3
    education = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school','Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
    # edu = data.loc[data[0]>25,colEdu]
    eduDict = {}
    deltaU = 1
    epsilon = [0.5, 1]
    for e in education:
        edu = data.loc[data[colEdu] == e, colEdu]
        eduDict[e] = len(edu.index)

    eduDict = [{key:math.exp((epsilon*value)/2) for (key, value) in eduDict.items()} for epsilon in epsilon]
    summary = sum(eduDict.values())
    eduProDict = {key:value/summary for (key, value) in eduDict.items()}
    np.random.choice(eduProDict.keys(), p = eduProDict.values())
    print()
    # print('probabilities = {}'.format(eduProDict))
    # b = [(e, GS/e) for e in epsilon]
    # variance = [(x[0], 2*(x[1]**2)) for x in b]
    # print("variance for different epsilon: {}".format(variance))
    # average_age = sum(cols)/len(cols.index)
    # resultWithNoise = [(epsilon, average_age + laplaceNoise(average_age, GS, epsilon)) for epsilon in epsilon]
    # print("result of querying avarage age that is over 25 with noise for differet epsilon: {}".format(resultWithNoise))

if __name__ == '__main__':
    resultWithNoise()