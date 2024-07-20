# Polynomial Regression

'''
    Importing the libraries

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

''' 
    Importing the dataset

'''

dataset = pd.read_csv(r"C:\Users\ujjwa\Documents\Position_Salaries.csv")
x = dataset.iloc[ :  , 1 : -1].values # We are skipping the starting column or 0th column because the 0th column and 1th column are having redundant data, means that the 1th column will do the work of 0th column that's why no need to add 0th column here.
y = dataset.iloc[ : , -1].values

'''
    Training the Linear Regression model on the whole dataset

'''

from sklearn.linear_model import LinearRegression
lin_regressor = LinearRegression()
lin_regressor.fit(x , y) # Now our model is trained on this given data / whole data 'x' and 'y'.

'''
    Training the Polynomial Regression model on the whole dataset

'''

from sklearn.preprocessing import PolynomialFeatures
# Object of PolynomialFeatures class
poly_regressor = PolynomialFeatures(degree = 4) 
x_poly = poly_regressor.fit_transform(x) 
lin_regressor_2 = LinearRegression() 
lin_regressor_2.fit(x_poly , y) # Now, we have our Polynomial Regression Model.

'''
    Visualising the Linear Regression results

'''

plt.scatter(x , y , color = 'red') # For real position levels and real salaries, it will plot a 2-d graph.
plt.plot(x , lin_regressor.predict(x) , color = "green")
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Levels')
plt.ylabel('Salary')
plt.show()

'''
    Visualising the Polynomial Regression results

'''

plt.scatter(x , y , color = "red")
plt.plot(x , lin_regressor_2.predict(poly_regressor.fit_transform(x)) , color = "green")
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

'''
    Visualising the Polynomial Regression results (for higher resolution and smoother curve)

'''

# For higher resolution and smoother curve:-
x_grid = np.arange(min(x) , max(x) , 0.1)
x_grid = x_grid.reshape(len(x_grid) , 1)
plt.scatter(x , y , color = 'red')
plt.plot(x_grid , lin_regressor_2.predict(poly_regressor.fit_transform(x_grid)) , color = 'green')
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel('Position level')
plt.ylabel('Salaries')
plt.show()

'''
    Predicting a new result with Linear Regression

'''
print("\n")
print('Predicted results (Linear Regression): ' , lin_regressor.predict([[6.5]]))

'''
    Predicting a new result with Polynomial Regression

'''
print("\n")
print('Predicted results (Polynomial Regression): ' , lin_regressor_2.predict(poly_regressor.fit_transform([[6.5]])))
print("\n")