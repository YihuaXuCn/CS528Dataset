import pandas as pd
import numpy as np
import mpmath as mp


def expM4Q2(epsilon):
  data = pd.read_csv('adult.data', sep=', ', header=None, engine='python')
  colEdu = 3
  education = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school','Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
  # edu = data.loc[data[0]>25,colEdu]
  eduDict = {}
  deltaU = 1
  mp.dps = 1000
  
  for e in education:
      edu = data.loc[data[colEdu] == e, colEdu]
      eduDict[e] = len(edu.index)

  eduDict = {key:mp.exp((epsilon*value)/2) for (key, value) in eduDict.items()}
  # print(eduDict)
  summary = sum(eduDict.values())
  # print(summary)
  eduProDict = {key:value/summary for (key, value) in eduDict.items()}
  # print(eduProDict)
  # print(sum(eduProDict.values()))
  y = np.random.choice(list(eduProDict.keys()), p = list(eduProDict.values()))
  return y


if __name__ == '__main__':
    epsilon = [0.5, 1]
    ret = [ expM4Q2(e) for e in epsilon]
    print(ret)