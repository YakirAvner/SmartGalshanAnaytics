import sqlite3
import pandas as pd
import csv
import os
import glob

class DBConnector:
    def __init__(self, df):
        self.df = df
    
    def load_databases(self): 
        # Connecting to each DB in the list.
        # Define the database connector pattern with wildcards
        db_connector_pattern = r"C:\Users\user\Desktop\Yakir Avner\DBTraining\Galshan*\Galshan*DB"
        print(f"db_connector_pattern: {db_connector_pattern}")
        db_files = glob.glob(os.path.join(
            db_connector_pattern, '**', 'Galshan*.db'), recursive=True)
        self.df.to_csv('data.csv', index=False)
        for dbName in db_files:
            try:
                conn = sqlite3.connect(dbName)
                conn.row_factory = sqlite3.Row  # 👈 THIS makes rows behave like dictionaries
                if conn:
                    print("Connected to SQLite")
                    max_temperature = conn.cursor()
                    time_max_temperature = conn.cursor()
                    num_of_detections = conn.cursor()

                    # MT abbreviation: Max Temperature.
                    MT = max_temperature.execute(
                        "SELECT MAX(Device_Temperature) from Snapshots;").fetchone()[0]

                    # TMT abbreviation: Time of Max Temperature.
                    TMT = time_max_temperature.execute("""
                                                        SELECT time
                                                        FROM Snapshots
                                                        WHERE device_temperature = (SELECT MAX(device_temperature) FROM Snapshots)
                                                                LIMIT 1;
                                                        """).fetchone()[0]
                    # Counting the number of detections.
                    num_of_detections = num_of_detections.execute(
                        "SELECT COUNT(*) from Detections").fetchone()[0]

                    self.df.loc[len(self.df)] = [dbName, MT, TMT, num_of_detections]
                self.df.to_csv('data.csv', index=False)
            except sqlite3.Error as e:
                print(f"Failed to connect to SQLite db: {dbName}")
            finally:
                if conn:    
                    conn.close()
                   
    def save(self, filename='data.csv'):
        self.df.to_csv(filename, index=False)