
# coding: utf-8

# In[ ]:

# loading csv file
from azureml import Workspace

ws = Workspace()
ds = ws.datasets['train.csv']
train = ds.to_dataframe()

ws1 = Workspace()
ds1 = ws1.datasets['test.csv']
test = ds1.to_dataframe()


# In[216]:

#Import libraries

import numpy as np
from numpy.random import random_integers
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from scipy.stats import pointbiserialr, spearmanr
get_ipython().magic(u'matplotlib inline')

print('Libraries Ready!')


# In[217]:

train.info()
#Age, Cabin and Embarked has missing value
#Age is hanlding missing value using mean imputation
#Embarked is hanlding missing value using mode imputation
#Cabin don't need to handling
train['Age']=train['Age'].fillna(value=train.Age.mean())
train['Embarked']=train['Embarked'].fillna(value=train.Embarked.mode())
train.info()


# In[255]:

#first, using univariate analysis

#1.gender
a=train['Survived'].groupby([train['Sex']]).count()
b=train['Survived'].groupby([train['Sex']]).sum()
c=b/a
print c
#2.age
def Age_filler(row):
    if row<18 :
        age=0
        return age
    elif row>=18 :
        age=1
        return age
    
train['Age2'] = train['Age'].apply(lambda x: Age_filler(x)) 
a=train['Survived'].groupby([train['Age2']]).count()
b=train['Survived'].groupby([train['Age2']]).sum()
c=b/a
print c

a=train['Survived'].groupby([train['Sex'],train['Age2']]).count()
b=train['Survived'].groupby([train['Sex'],train['Age2']]).sum()
c=b/a
print c

#3.P-Class
a=train['Survived'].groupby([train['Pclass']]).count()
b=train['Survived'].groupby([train['Pclass']]).sum()
c=b/a
print c

a=train['Survived'].groupby([train['Sex'],train['Pclass'],train['Age2']]).count()
b=train['Survived'].groupby([train['Sex'],train['Pclass'],train['Age2']]).sum()
c=b/a
print c
#high correlation fare and p-class
train['Fare'].groupby([train['Survived'], train['Pclass']]).mean()

#4.Embarked
a=train['Survived'].groupby([train['Embarked']]).count()
b=train['Survived'].groupby([train['Embarked']]).sum()
c=b/a
print c

a=train['Survived'].groupby([train['Sex'],train['Pclass'],train['Embarked'],train['Age2']]).count()
b=train['Survived'].groupby([train['Sex'],train['Pclass'],train['Embarked'],train['Age2']]).sum()
c=b/a
print c

def estimate(row):
    if row.Sex=='female' and row.Pclass==1:
        estimate=1
        return estimate
    elif row.Sex=='female' and row.Pclass==2:
        estimate=1
        return estimate
    elif row.Sex=='female' and row.Pclass==3 and row.Embarked=='C' and row.Age<18:
        estimate=1
        return estimate
    elif row.Sex=='female' and row.Pclass==3 and row.Embarked=='Q':
        estimate=1
        return estimate
    elif row.Sex=='male' and row.Pclass==1 and row.Age<18:
        estimate=1
        return estimate
    elif row.Sex=='male' and row.Pclass==2 and row.Age<18:
        estimate=1
        return estimate
    else :
        estimate=0
        return estimate
#Simulation
train["Survived_yn1"]  = train.apply(estimate, axis = 1)
train_simulation=train['Survived'].groupby([train['Survived'],train['Survived_yn1']]).count()
print train_simulation

test["Survived"]  = test.apply(estimate, axis = 1)
#test_simulation=test['Survived_yn1'].groupby([test['Survived_yn1']]).count()
#print "*test simulation"
#print test_simulation

test

#test2.to_csv("test10.csv",index = False)


# In[240]:

#second, logistic model
from sklearn.linear_model import LogisticRegression
RegModel=LogisticRegression()
x=train[["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]]
y=array(train.Survived)
#y=column_or_1d(y,warn=True)
RegModel=RegModel.fit(x,y)
#y,x=dmatrices('Survived ~ +Pclass + Sex + Age + SibSp + Parch + Fare + Embarked',train,return_type="dataframe")

