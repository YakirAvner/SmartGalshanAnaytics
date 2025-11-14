import Month_Day_Separation as mds
import DB_Connector as dbc
import pandas as pd

# If the program is running in the main file, then:
if __name__ == "__main__":
    df = pd.DataFrame(columns=["DBName", "MaxTemp", "TimeMaxTemp", "NumDetections"])

    connector = dbc(df)
    connector.load_databases()   # fills df and writes data.csv
    # or later:
    connector.save("my_data.csv")
        
        
        
        
        # data = {
        #     'Database': [],
        #     'Max_Temperature': [],
        #     'Time_of_Max_Temperature': [],
        #     'Number_of_Detections': []
        # }
        # df = pd.DataFrame(data)
        # month_day_separator = mds.MonthDaySeparation(df)
        # db_connector = dbc.DBConnector(df)

