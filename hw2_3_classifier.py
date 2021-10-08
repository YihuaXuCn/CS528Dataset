import pandas as pd
import math
import numpy as np

def expM4Q3(epsilon, groundTruth):
  irisType = [0,1,2]
  typesDict = {t:len([e for e in groundTruth if e == t]) for t in irisType}
  deltaU = 1
  typesDict = {key:math.exp((epsilon*value)/(2*deltaU)) for (key, value) in typesDict.items()}

  summary = sum(typesDict.values())

  typeProbDict = {key:value/summary for (key, value) in typesDict.items()}

  y = np.random.choice(list(typeProbDict.keys()), len(groundTruth), p = list(typeProbDict.values()))
  return y

if __name__ == '__main__':
    
    data = pd.read_csv('iris.data', sep=',', header=None, engine='python')
    irisTypeDict = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
    dataSetosa = data.loc[data[4]=='Iris-setosa', :]
    dataSetosa[4] = irisTypeDict['Iris-setosa']
    dataVersicolor = data.loc[data[4]=='Iris-versicolor',:]
    dataVersicolor[4] = irisTypeDict['Iris-versicolor']
    dataVirginica = data.loc[data[4]=='Iris-virginica',:]
    dataVirginica[4] = irisTypeDict['Iris-virginica']
    # print(dataSetosa, dataVersicolor, dataVirginica)
    dataTest = pd.concat([dataSetosa[:10],dataVersicolor[:10],dataVirginica[:10]])
    xTest = dataTest.loc[:,[0,1,2,3]]
    yTest = dataTest.loc[:,[4]]
    dataTrain = pd.concat([dataSetosa[10:],dataVersicolor[10:],dataVirginica[10:]])
    xTrain = dataTrain.loc[:,[0,1,2,3]]
    yTrain = dataTrain.loc[:,[4]]
    # print(xTrain.shape, yTrain, yTrain.to_numpy())

    from sklearn import datasets
    from sklearn import metrics
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import classification_report

    model = GaussianNB()
    model.fit(xTrain, yTrain.to_numpy().reshape((yTrain.shape[0],)))
    expected = yTest.to_numpy().reshape((yTest.shape[0],))
    predicted = model.predict(xTest)
    # print(expected.shape, predicted.shape)
    # print(classification_report(expected, predicted))
    epsilon = [0.5, 1, 2, 4, 8, 16]
    predWithNoise = [expM4Q3(epsilon, predicted) for epsilon in epsilon]
    predWithNoise
    results = [classification_report(expected, pwn) for pwn in predWithNoise]
    [print(r) for r in results]