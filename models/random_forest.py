
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from joblib import dump, load

class RandomForestRegression:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=50, max_depth=5, min_samples_split=2)
        
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        
    def predict(self, X_test):
        return self.model.predict(X_test)
    
    def accuracy(self, y_test, predictions):
        return mean_squared_error(y_test, predictions)
    
    def save_model(self, file_path):
        # Save the trained model to a file
        dump(self.model, file_path)
        
    def load_model(self, file_path):
        # Load a trained model from a file
        self.model = load(file_path)