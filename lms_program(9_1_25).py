# -*- coding: utf-8 -*-
"""LMS_Program(9-1-25).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A0xNYrRqxOGbYg0tdxbpCmYjnqj7CVNI

# Date : 9-1-25
# Importing a CSV file
"""

import pandas as pd
df = pd.read_csv(r'/content/purchases.csv')
print(df.head(10))

"""# Plotting"""

import matplotlib.pyplot as plt
#Scatter plot for purchases
plt.figure(figsize=(5,4)) # Changed fig_size to figsize, passing tuple directly
plt.scatter(df['Age'],df['Purchased'], cmap='bwr', label= 'Purchased')
plt.xlabel('Age')
plt.ylabel('Purchased(0 = No, 1 = Yes)')
plt.title('New Project')
plt.legend(['No purchase','Purchase'])
plt.grid(True)

"""# Prediction using Logistic regression model"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
x = df[['Age']]
y = df[['Purchased']]
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2, random_state=42)
model=LogisticRegression()
model.fit(x_train,y_train)
#prediction
new_age=[[20]]
prediction = model.predict(new_age)
probability = model.predict_proba(new_age)
print(f"Prediction for Age {new_age[0][0]}: {'will purchase' if prediction[0]==1 else 'will not purchase'}")
print(f"Probability of purchasing: {probability[0][1]}")