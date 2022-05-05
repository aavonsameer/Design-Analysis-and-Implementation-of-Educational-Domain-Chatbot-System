import pandas as pd

read_file = pd.read_excel (input("data2")+'.xlsx')
read_file.to_csv (input("data2")+'.csv', index = None, header=True)