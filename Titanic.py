import math
import numpy as np 
import pandas as pd 
import seaborn as sns 
from seaborn import countplot 
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure, show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def TitanicLogistic():
    # step 1 : Load data
    titanic_data = pd.read_csv('TitanicDataset.csv')

    print("First 5 entries from loaded dataset")
    print(titanic_data.head())

    print("Number of passangers are "+str(len(titanic_data)))

    # step 2 : Analyze data
    print("Visualisation : Survived and non survied passangers")
    figure()
    target = "Survived"

    countplot(data=titanic_data, x=target).set_title("Survived and non survied passangers")
    show()

    print("Visualisation : Survived and non survied passangers based on Gender")
    figure()
    target = "Survived"

    countplot(data=titanic_data, x=target, hue="Sex").set_title("Survived and non survied passangers based on Gender")
    show()

    print("Visualisation : Survived and non survied passangers based on the passanger class")
    figure()
    target = "Survived"

    countplot(data=titanic_data, x=target, hue="Pclass").set_title("Survived and non survied passangers based on the Passanger class")
    show()

    print("Visualisation : Survived and non survied passangers based on Age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Survived and non survied passangers based on Age")
    show()

    print("Visualisation : Survived and non survied passangers based on the Fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Survived and non survied passangers based on Fare")
    show()

    # step3 : Data Cleaning
    titanic_data.drop("zero",axis = 1, inplace = True)

    print("First 5 entries from loaded dataset after removing zero column")
    print(titanic_data.head(5))

    print("Values of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of Sex column after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"], drop_first = True)
    print(Sex.head(5))

    print("Values of Pclass column after removing one field")
    Pclass = pd.get_dummies(titanic_data["Pclass"], drop_first = True)
    print(Pclass.head(5))

    print("Values of data set after concatenating new columns")
    titanic_data = pd.concat([titanic_data,Sex,Pclass],axis =1)
    print(titanic_data.head(5))

    print("Values of data set after removing irrelevent columns")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"], axis = 1, inplace = True)
    print(titanic_data.head(5))

    x = titanic_data.drop("Survived",axis = 1)
    y = titanic_data["Survived"]

    # step4 : Data Training
    xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size = 0.5)

    logmodel = LogisticRegression()

    logmodel.fit(xtrain,ytrain)

    # step5 : Data Testing
    prediction = logmodel.predict(xtest)

    # step6 : Calculate Accuracy
    print("Classification report of Logistic Regression is : ")
    print(classification_report(ytest,prediction))

    print("Confusion Matrix of Logistic Regression is : ")
    print(confusion_matrix(ytest,prediction))

    print("Accuracy of Logistic Regression is : ")
    print(accuracy_score(ytest,prediction))

def main():
    print("----Titanic Survival Predictor----")

    print("Supervised Machine Learning")

    print("Logistic Regression on Titanic data set")

    TitanicLogistic()

if __name__ == "__main__":
    main()