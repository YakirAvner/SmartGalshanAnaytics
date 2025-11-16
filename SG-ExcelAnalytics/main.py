import Month_Day_Separation as mds
from DB_Connector import DBConnector as dbc
import pandas as pd

# If the program is running in the main file, then:
if __name__ == "__main__":
    df = pd.DataFrame(columns=["DBName", "MaxTemp",
                      "TimeMaxTemp", "NumDetections"])
    connector = dbc(df)
    connector.load_databases()  # fills df and writes data.csv
    connector.save('data.csv', 'data.xlsx')  # saves data.csv and data.xlsx
    df

    # data = {
    #     'Database': [],
    #     'Max_Temperature': [],
    #     'Time_of_Max_Temperature': [],
    #     'Number_of_Detections': []
    # }
    # df = pd.DataFrame(data)
    # month_day_separator = mds.MonthDaySeparation(df)
    # db_connector = dbc.DBConnector(df)
