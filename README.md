# Polynomial Regression

This repository contains a Python implementation of Polynomial Regression to predict salaries based on position levels. The dataset used for this example is a fictional dataset of positions and their corresponding salaries. The purpose of this project is to demonstrate how Polynomial Regression can be used to model non-linear relationships in data.

## Table of Contents:

- Introduction
- Dependencies
- Dataset
- Code Explanation
- Results
- Conclusion

## Introduction:

Polynomial Regression is an extension of Linear Regression, where the relationship between the independent variable and the dependent variable is modeled as an nth degree polynomial. This allows for better fitting of non-linear data compared to a simple linear model.

## Dependencies:

To run this code, you need the following Python libraries:

- pandas
- numpy
- matplotlib
- scikit-learn


## Dataset:

The dataset used in this project is Position_Salaries.csv, which contains two main columns: Position and Salary. The Position column represents different job positions, and the Salary column represents the corresponding salaries for those positions.

## Code Explanation:

### Importing the Libraries:-

We import pandas for data manipulation, numpy for numerical operations, and matplotlib.pyplot for plotting graphs.

### Importing the Dataset:-

We read the dataset and extract the independent variable x (Position Levels) and the dependent variable y (Salaries).

### Training the Linear Regression Model:-

We create a Linear Regression model and fit it to the entire dataset. This model will be used to compare with Polynomial Regression.

### Training the Polynomial Regression Model:-

We create a Polynomial Regression model with a degree of 4, transform the independent variable x into polynomial features, and fit a Linear Regression model to these features.

### Visualising the Results:-

- Linear Regression:

We plot the original data points in red and the Linear Regression line in green to visualize how well the Linear Regression model fits the data.

- Polynomial Regression:

We plot the original data points in red and the Polynomial Regression curve in green to visualize the better fit of the Polynomial model.

- Polynomial Regression (Higher Resolution and Smoother Curve):

To get a smoother curve, we increase the resolution by creating a grid of values for x and plot the Polynomial Regression predictions.

### Predicting New Results:-

- Linear Regression:

We predict the salary for a position level of 6.5 using the Linear Regression model.

- Polynomial Regression:

We predict the salary for a position level of 6.5 using the Polynomial Regression model.

### Results:-

The results show that Polynomial Regression provides a much better fit for the dataset compared to Linear Regression, especially when visualized with a higher resolution and smoother curve. The predicted salaries using Polynomial Regression are closer to the actual salaries, demonstrating its effectiveness in modeling non-linear relationships.

## Conclusion:

Polynomial Regression is a powerful tool for modeling non-linear relationships in data. This project demonstrates how to implement and visualize Polynomial Regression using Python. By comparing it with Linear Regression, we can see the advantages of using a more flexible model for non-linear data.