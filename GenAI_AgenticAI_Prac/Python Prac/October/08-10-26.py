import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
dataset = pd.read_csv(r"C:\Users\polin\Desktop\GenAI_AgenticAI_Prac\Python Prac\October\Salary_Data.csv")

x = dataset.iloc[:, :-1]  
y = dataset.iloc[:, -1] 


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, 
                                                    test_size=0.20,
                                                    random_state=0) 

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train) 

y_pred = regressor.predict(x_test) 

# Compare predicted and actual salaries from the test set
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison) 

plt.scatter(x_test, y_test, color = 'red')  # Real salary data (testing)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Regression line from training set
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary') 
plt.show()  

m_slope = regressor.coef_ 
print(m_slope)

c_inter = regressor.intercept_
print(c_inter) 

emp_exp_12 = m_slope*12+c_inter
print(emp_exp_12) 

emp_exp_20 = m_slope*20+c_inter
print(emp_exp_20) 

bias = regressor.score(x_train, y_train)
print(bias)

var = regressor.score(x_test, y_test)
print(var)

dataset.mean()
dataset['Salary'].mean()
dataset.median()
dataset['Salary'].mode()
dataset.describe()
dataset.var()
dataset.std()
dataset.corr()
dataset.skew()

# Anova -- SSR, SST, SSE

#SSR
y = y[0:6]
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

#SSE
y = y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)

#SST
mean_tota = np.mean(dataset.values)
SST = np.sum((dataset.values-mean_total)**2)
print(SST)

import pickle
filename = "linear_regression_model.pkl"
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
    print("Model has been pickled and saved as linear_regression_model.pkl")
    
import os
print(os.getcwd())





