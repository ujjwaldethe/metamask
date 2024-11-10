import pandas as pd
//pip install tensorflow
df = pd.read_csv('Churn_Modelling.csv')
df.shape
print(df.head())

from sklearn.model_selection import train_test_split
# Define features and target
X = df.drop(columns=['Exited', 'CustomerId'])  # 'Exited' is the target variable
y = df['Exited']
# Step 2: Convert categorical variables to dummy/indicator variables
X = pd.get_dummies(X, drop_first=True)
# Step 3: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training set shape: {X_train.shape}, Test set shape: {X_test.shape}")

from sklearn.preprocessing import StandardScaler
# Step 4: Normalize the Train and Test Data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(f"Mean of X_train: {X_train.mean(axis=0)}, Variance of X_train: {X_train.var(axis=0)}")

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# Step 5: Initialize and Build the Model
model = keras.Sequential([
    layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # For binary classification
])
# Step 6: Compile the Model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# Step 7: Train the Model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)
# Step 8: Output Training History
print(history.history)

from sklearn.metrics import accuracy_score, confusion_matrix
# Make predictions
y_pred = (model.predict(X_test) > 0.5).astype("int32")
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
# Print confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

