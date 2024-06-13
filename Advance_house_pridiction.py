import matplotlib.pyplot as plt
#%matplotlib inline 
import numpy as np
import pandas as pd
import seaborn as sns
from io import BytesIO,StringIO

###########IF YOU WANT ANOTHER DATA EXCEPT TRAIN.CSV THEN USE THIS COMMENTED OUT ALGORITHM AND ADD DATA ACCORDING AND COMMENTED OUT THE CODE IN WHICH TRAIN.CSV IS CALLED FOR ANALYSIS 

#b=open('C:\CODING FOLDER\coding files of python\PYTHONCODE\codes2\titanic_train.csv')
# train=('PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked\n'
# '1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S\n'
# '2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C\n'
# '3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S\n'
# '4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S\n'
# '5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S\n'
# '6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q\n'
# '7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S\n'
# '8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,21.075,,S\n'
# '9,1,3,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",female,27,0,2,347742,11.1333,,S\n'
# '10,1,2,"Nasser, Mrs. Nicholas (Adele Achem)",female,14,1,0,237736,30.0708,,C\n')
# print(StringIO(train))
# train= pd.read_csv(StringIO(train))
# print(train)
################################

pd.pandas.set_option('display.max_columns',None)
dataset= pd.read_csv('C:/CODING FOLDER/coding files of python/Pythoncode/codes2/train.csv')## PLEASE PROVIDE LOCAL ADDRESS OF THE FILE IN YOU LAPTOP AND PC 
print(dataset.shape)

###############print the top5.shape
print(dataset.shape)
b=dataset.head()
print(b)

#here we will check the percentage of non values present in each feature 
#!1 -step make the list of features in dataset.column if dataset[features].
#2- step print the feature name and the percentage of missing values 

feature_with_na=[features for features in dataset.columns if dataset[features].isnull().sum()<1]
for feature in feature_with_na:
    print(feature,np.round(dataset[feature].isnull().mean(),4),'% missing values')
    
    # since there are many missing values, we need to find the relationship betweeen missing values and sales price

for feature in feature_with_na:
    data=dataset.copy()
    data[feature]=np.where(data[feature].isnull(),1,0)
    #lets calculate the mean salesprice where the information is missing or 
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.title(feature)
    plt.show()
    plt.savefig('firstprojectbarplot1.png')
    plt.savefig('firstprojectbarplot2.png')
    plt.savefig('firstprojectbarplot3.png')
print("Id of houses{}".format(len(dataset.Id)))

######NUMERICAL VARIABLES###############
#LIST OF NUMERICAL VARIABLES

numerical_features = [feature for feature in dataset.columns if dataset[feature].dtype !='0']
print('number of numerical variables:', len(numerical_features))
#visualise the numerical variables

c=dataset[numerical_features].head()
print(c)
# lis tof the variables that contain year information 

year_feature =[feature for feature in numerical_features if 'yr'in feature.lower() or'year'in feature.lower()]

print(year_feature)
## let analysise the temporal variables
# ## we will check whether there is a relation between year and houses is sold and 

dataset.groupby('YrSold')['SalePrice'].median().plot()
plt.xlabel('year sold')
plt.ylabel('median house Price')
plt.title("house price Vs year sold ")
plt.show()
plt.savefig('first_plot5.png')

#@ here we will compare the difference between all years feature with YrSold 

for feature in year_feature:
    if feature!='YrSold':
        data=dataset.copy()
        ## we will capture the difference between year variable and year the house was sold for

        data[feature]=data['YrSold']-data[feature]
        plt.scatter(data[feature],data['SalePrice'])
        plt.xlabel(feature)
        plt.ylabel('SalePrice')
        plt.show()
        plt.savefig('first_plot6.png')
        plt.savefig('first_plot7.png')
        plt.savefig('first_plot8.png')
        plt.savefig('first_plot9.png')
        plt.savefig('first_plot10.png')
        plt.savefig('first_plot11.png')
        plt.savefig('first_plot12.png')
        plt.savefig('first_plot13.png')
        plt.savefig('first_plot14.png')
        
        #######descrete_variable############
        #discrete variables are variables that have a finite number of values

discrete_feature=[feature for feature in numerical_features if len(dataset[feature].unique())<25 and feature not in year_feature+['Id']]
print("Discrete Variables Count: {}".format(len(discrete_feature)))
for feature in discrete_feature:
    data=dataset.copy()
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    plt.show()
    plt.savefig('first_plot15.png')
    plt.savefig('first_plot16.png')
    plt.savefig('first_plot17.png')
    plt.savefig('first_plot18.png')
    plt.savefig('first_plot19.png')

            #####CONTINUOUS VARIABLES#######

continuous_feature=[feature for feature in numerical_features if feature not in discrete_feature+year_feature+['Id']]
print("Continuous feature Count {}".format(len(continuous_feature)))
for feature in continuous_feature:
    data=dataset.copy()
    data[feature].hist(bins=25)
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.title(feature)
    plt.show()
    plt.savefig('first_plot20.png')
    plt.savefig('first_plot21.png')
    plt.savefig('first_plot22.png')
    plt.savefig('first_plot23.png')
    plt.savefig('first_plot24.png')
    plt.savefig('first_plot25.png')
    plt.savefig('first_plot26.png')
            
            
#### we will be using logarthmic transformation##########

for feature in continuous_feature:
    data=dataset.copy()
    if 0 in data[feature].unique():
        pass 
    else:
        data[feature]=np.log(data[feature])
        data['SalePrice']=np.log(data['SalePrice'])
        plt.scatter(data[feature], data['SalePrice'])
        plt.xlabel('feature')
        plt.ylabel('SalePrice') 
        plt.title(feature)
        plt.show()
        
        
        ###categorical variables#########

categorical_features= [feature for feature in dataset.columns if dataset[feature].dtypes =='0']
print(categorical_features)    
d= dataset[categorical_features].head() 
print(d)  
for feature in categorical_features:
    print('The feature is {} and number of categories are {}'.format(feature, dataset[feature].unique()))

    #### find the relationship between categorical_features and dependent_features

for feature in categorical_features:
    data=dataset.copy()
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    plt.show()
    plt.savefig('first_plot27.png')
    plt.savefig('first_plot28.png')
    plt.savefig('first_plot29.png')
    plt.savefig('first_plot30.png')
    plt.savefig('first_plot31.png')
    plt.savefig('first_plot32.png')
    plt.savefig('first_plot33.png')
    plt.savefig('first_plot34.png')
    plt.savefig('first_plot35.png')
    plt.savefig('first_plot36.png')
    plt.savefig('first_plot37.png')