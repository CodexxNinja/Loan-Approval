import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
# Load Dataset
data = pd.read_csv("dataset/train.csv")

# Separate Features and Target
X = data.drop(
    ["loan_status", "cb_person_default_on_file"],
    axis=1
)

y = data["loan_status"]

# Label Encoding
label_encoder = LabelEncoder()

X["person_home_ownership"] = label_encoder.fit_transform(
    X["person_home_ownership"]
)

X["loan_intent"] = label_encoder.fit_transform(
    X["loan_intent"]
)

X["loan_grade"] = label_encoder.fit_transform(
    X["loan_grade"]
)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# Model Training
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy Score:")
print(accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Classification Report
report = classification_report(y_test, y_pred)

print("\nClassification Report:")
print(report)

# Correct Predictions
correct_predictions = (y_test == y_pred).sum()

print("\nCorrect Predictions:")
print(correct_predictions)

# Incorrect Predictions
incorrect_predictions = (y_test != y_pred).sum()

print("\nIncorrect Predictions:")
print(incorrect_predictions)
