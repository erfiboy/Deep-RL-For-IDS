import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
def load_datasets():
    path = './Dataset/Processed_IoT_dataset'
    for file in os.listdir(path=path):
        file_path = os.path.join(path, file)
        
        if file == 'IoT_Weather.csv':
            IoT_Weather = pd.read_csv(file_path)
            
        if file == 'IoT_Thermostat.csv':
            IoT_Thermostat = pd.read_csv(file_path)
            
        if file == 'IoT_Garage_Door.csv':
            IoT_Garage_Door = pd.read_csv(file_path)
            
        if file == 'IoT_Fridge.csv':
            IoT_Fridge = pd.read_csv(file_path)
            
        if file == 'IoT_Modbus.csv':
            IoT_Modbus = pd.read_csv(file_path)
            
        if file == 'IoT_Motion_Light.csv':
            IoT_Motion_Light = pd.read_csv(file_path)
            
        if file == 'IoT_GPS_Tracker.csv':
            IoT_GPS_Tracker = pd.read_csv(file_path)
            
    return IoT_Weather, IoT_Thermostat, IoT_Garage_Door, IoT_Fridge, IoT_Modbus, IoT_Motion_Light, IoT_GPS_Tracker
        
IoT_Weather, IoT_Thermostat, IoT_Garage_Door, IoT_Fridge, IoT_Modbus, IoT_Motion_Light, IoT_GPS_Tracker = load_datasets()

def process_IoT_Weather(IoT):
    IoT['temp_condition'] = 'not_applicable'
    IoT['door_state'] = 'state_false'
    IoT['sphone_signal'] = False
    IoT['latitude'] = -999
    IoT['longitude'] = -999
    IoT['FC1_Read_Input_Register'] = -999
    IoT['FC2_Read_Discrete_Value'] = -999
    IoT['FC3_Read_Holding_Register'] = -999 
    IoT['FC4_Read_Coil'] = -999
    IoT['motion_status'] = -999
    IoT['light_status'] = 'status_false'
    IoT['thermostat_status'] = -999
    IoT['Weather'] = 1
    IoT['Thermostat'] = 0
    IoT['Garage_Door'] = 0
    IoT['Fridge'] = 0
    IoT['Modbus'] = 0
    IoT['Motion_Light'] = 0
    IoT['GPS_Tracker'] = 0
    

def process_IoT_Thermostat(IoT):
    IoT['temp_condition'] = 'not_applicable'
    IoT['door_state'] = 'state_false'
    IoT['sphone_signal'] = False
    IoT['latitude'] = -999
    IoT['longitude'] = -999
    IoT['FC1_Read_Input_Register'] = -999
    IoT['FC2_Read_Discrete_Value'] = -999
    IoT['FC3_Read_Holding_Register'] = -999 
    IoT['FC4_Read_Coil'] = -999
    IoT['motion_status'] = -999
    IoT['light_status'] = 'status_false'
    IoT['pressure'] = -999
    IoT['humidity'] = -999
    IoT['Weather'] = 0
    IoT['Thermostat'] = 1
    IoT['Garage_Door'] = 0
    IoT['Fridge'] = 0
    IoT['Modbus'] = 0
    IoT['Motion_Light'] = 0
    IoT['GPS_Tracker'] = 0
    IoT.rename(columns={'current_temperature': 'temperature'}, inplace=True)
    
    

def process_IoT_Garage_Door(IoT):
    IoT['temperature'] = -999
    IoT['temp_condition'] = 'not_applicable'
    IoT['latitude'] = -999
    IoT['longitude'] = -999
    IoT['FC1_Read_Input_Register'] = -999
    IoT['FC2_Read_Discrete_Value'] = -999
    IoT['FC3_Read_Holding_Register'] = -999 
    IoT['FC4_Read_Coil'] = -999
    IoT['motion_status'] = -999
    IoT['light_status'] = 'status_false'
    IoT['thermostat_status'] = -999
    IoT['pressure'] = -999
    IoT['humidity'] = -999
    IoT['Weather'] = 0
    IoT['Thermostat'] = 0
    IoT['Garage_Door'] = 1
    IoT['Fridge'] = 0
    IoT['Modbus'] = 0
    IoT['Motion_Light'] = 0
    IoT['GPS_Tracker'] = 0
    IoT.dropna(subset=['sphone_signal'], inplace=True)
    
    for index, iot in IoT.iterrows():
        if iot['sphone_signal'] == 0 or iot['sphone_signal'] == '0':
            IoT.at[index, 'sphone_signal'] = 'false'
        
        if iot['sphone_signal'] == 1 or iot['sphone_signal'] == '1':
            IoT.at[index, 'sphone_signal'] = 'true'
            
    IoT['sphone_signal'] = IoT['sphone_signal'].astype(str)

def process_IoT_Fridge(IoT):
    IoT['door_state'] = 'state_false'
    IoT['sphone_signal'] = False
    IoT['latitude'] = -999
    IoT['longitude'] = -999
    IoT['FC1_Read_Input_Register'] = -999
    IoT['FC2_Read_Discrete_Value'] = -999
    IoT['FC3_Read_Holding_Register'] = -999 
    IoT['FC4_Read_Coil'] = -999
    IoT['motion_status'] = -999
    IoT['light_status'] = 'status_false'
    IoT['thermostat_status'] = -999
    IoT['pressure'] = -999
    IoT['humidity'] = -999
    IoT['Weather'] = 0
    IoT['Thermostat'] = 0
    IoT['Garage_Door'] = 0
    IoT['Fridge'] = 1
    IoT['Modbus'] = 0
    IoT['Motion_Light'] = 0
    IoT['GPS_Tracker'] = 0
    IoT.rename(columns={'fridge_temperature': 'temperature'}, inplace=True)

def process_IoT_Modbus(IoT):
    IoT['temperature'] = -999
    IoT['temp_condition'] = 'not_applicable'
    IoT['door_state'] = 'state_false'
    IoT['sphone_signal'] = False
    IoT['latitude'] = -999
    IoT['longitude'] = -999
    IoT['motion_status'] = -999
    IoT['light_status'] = 'status_false'
    IoT['thermostat_status'] = -999
    IoT['pressure'] = -999
    IoT['humidity'] = -999
    IoT['Weather'] = 0
    IoT['Thermostat'] = 0
    IoT['Garage_Door'] = 0
    IoT['Fridge'] = 0
    IoT['Modbus'] = 1
    IoT['Motion_Light'] = 0
    IoT['GPS_Tracker'] = 0

def process_IoT_Motion_Light(IoT):
    IoT['temperature'] = -999
    IoT['temp_condition'] = 'not_applicable'
    IoT['door_state'] = 'state_false'
    IoT['sphone_signal'] = False
    IoT['latitude'] = -999
    IoT['longitude'] = -999
    IoT['FC1_Read_Input_Register'] = -999
    IoT['FC2_Read_Discrete_Value'] = -999
    IoT['FC3_Read_Holding_Register'] = -999 
    IoT['FC4_Read_Coil'] = -999
    IoT['thermostat_status'] = -999
    IoT['pressure'] = -999
    IoT['humidity'] = -999
    IoT['Weather'] = 0
    IoT['Thermostat'] = 0
    IoT['Garage_Door'] = 0
    IoT['Fridge'] = 0
    IoT['Modbus'] = 0
    IoT['Motion_Light'] = 1
    IoT['GPS_Tracker'] = 0

def process_IoT_GPS_Tracker(IoT):
    IoT['temperature'] = -999
    IoT['temp_condition'] = 'not_applicable'
    IoT['door_state'] = 'state_false'
    IoT['sphone_signal'] = False
    IoT['FC1_Read_Input_Register'] = -999
    IoT['FC2_Read_Discrete_Value'] = -999
    IoT['FC3_Read_Holding_Register'] = -999 
    IoT['FC4_Read_Coil'] = -999
    IoT['motion_status'] = -999
    IoT['light_status'] = 'status_false'
    IoT['thermostat_status'] = -999
    IoT['pressure'] = -999
    IoT['humidity'] = -999
    IoT['Weather'] = 0
    IoT['Thermostat'] = 0
    IoT['Garage_Door'] = 0
    IoT['Fridge'] = 0
    IoT['Modbus'] = 0
    IoT['Motion_Light'] = 0
    IoT['GPS_Tracker'] = 1
    
def concatenate_data_frames(IoT_Fridge, IoT_Garage_Door, IoT_GPS_Tracker, IoT_Modbus, IoT_Motion_Light, IoT_Thermostat, IoT_Weather):
    df_concatenated = pd.concat([IoT_Fridge, IoT_Garage_Door, IoT_GPS_Tracker, IoT_Modbus, IoT_Motion_Light, IoT_Thermostat, IoT_Weather])
    df_concatenated['sphone_signal'] = df_concatenated['sphone_signal'].astype(str)
    df_concatenated.to_csv('./Dataset/Processed_IoT_dataset/IoT_concatenated.csv')
    return df_concatenated

def one_hot_encoding(IoT):
    IoT.drop(['date', 'time'], axis=1, inplace=True)
    categorical_features = ['temp_condition', 'type', 'door_state', 'sphone_signal', 'light_status']
    categorical_transformer = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    IoT_encoded = pd.DataFrame(categorical_transformer.fit_transform(IoT[categorical_features]))
    IoT_encoded.columns = categorical_transformer.get_feature_names_out(categorical_features)
    IoT.drop(categorical_features, axis=1, inplace=True)
    IoT = IoT.reset_index(drop=True)
    IoT_encoded = IoT_encoded.reset_index(drop=True)

    IoT = pd.concat([IoT, IoT_encoded], axis=1)
    IoT.to_csv('./Dataset/Processed_IoT_dataset/IoT_one_hot_encoded.csv')

    return IoT
 
    

process_IoT_Fridge(IoT_Fridge)
process_IoT_Garage_Door(IoT_Garage_Door)
process_IoT_GPS_Tracker(IoT_GPS_Tracker)
process_IoT_Modbus(IoT_Modbus)
process_IoT_Motion_Light(IoT_Motion_Light)
process_IoT_Thermostat(IoT_Thermostat)
process_IoT_Weather(IoT_Weather)
print(IoT_Garage_Door)
df = concatenate_data_frames(IoT_Fridge, IoT_Garage_Door, IoT_GPS_Tracker, IoT_Modbus, IoT_Motion_Light, IoT_Thermostat, IoT_Weather)
print(df.dtypes)
df_new = one_hot_encoding(df)
print(df_new)
