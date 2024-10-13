import os
import pandas as pd
from models.random_forest import *
def get_dataset():
    path = './Dataset/Processed_IoT_dataset/IoT_Preprocessed.csv'
    df = pd.read_csv(path)
    return df


def train(df):
    columns = df.columns
    features = [feature for feature in columns if feature not in ['Weather', 'Thermostat', 'Garage_Door', 'Fridge', 'Modbus', 'Motion_Light', 'GPS_Tracker']]
    X = df[features]
    Y = df[['Weather', 'Thermostat', 'Garage_Door', 'Fridge', 'Modbus', 'Motion_Light', 'GPS_Tracker']]
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    X_train = X_train.values
    X_test = X_test.values
    y_train = y_train.values
    y_test = y_test.values
    
    model = RandomForestRegression()
    print("Started Training: \n")
    
    model.train(X_train, y_train)
    
    model_file_path = './models/saved_models/random_forest.pkl'
    model.save_model(model_file_path)
    
    predictions = model.predict(X_test)
    
    mse = model.accuracy(y_test, predictions)
    
    print(mse)
    
train(get_dataset())