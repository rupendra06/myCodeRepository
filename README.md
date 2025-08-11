Objective
To implement and understand Simple and Multiple Linear Regression using a housing dataset.

Steps Taken
Loaded the dataset (Housing.csv)

Data contains features like area, bedrooms, bathrooms, location info, and price.

Preprocessed the data

Converted categorical columns (like mainroad, guestroom, etc.) into numbers using Label Encoding so the regression model can use them.

Simple Linear Regression

Used only area as the predictor for price.

Trained a model and generated a regression line.

Multiple Linear Regression

Used all features to predict price.

Trained another model and obtained coefficients for each feature.

Evaluated both models

Used Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² Score to measure accuracy.

Visualization

Plotted actual vs predicted values with the regression line for the simple model.

Results
Simple model: Shows the relationship between area and price but with limited accuracy.

Multiple model: Uses more data and gives a better prediction, but coefficients need interpretation to understand feature importance.
