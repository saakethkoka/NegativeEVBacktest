import pandas as pd

with open("/Users/saakethkoka/Documents/Stonks/DataSets/Compustat_Quarterly_Fundamentals.csv") as f:
    lines = f.readlines()
    headers = lines[0].split(",")
    for line in lines[:500]:
        print(line.strip())



# df = pd.read_csv ("/Users/saakethkoka/Documents/Stonks/DataSets/Compustat_Quarterly_Fundamentals.csv")