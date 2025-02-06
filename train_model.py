import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib

def train_model(data_path: str, model_path: str):
    """Loads processed data, trains a model, and saves it."""
    df = pd.read_csv(data_path)

    # Split data into features and target
    X = df.drop(columns=['y'])
    y = df['y'].apply(lambda x: 1 if x == 'yes' else 0)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Train a model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    print(f"Model Accuracy: {accuracy:.2f}")
    print(f"F1 Score: {f1:.2f}")

    # Save model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model("data/processed_data.csv", "models/bank_model.pkl")
