import pandas as pd
import numpy as np

dfa = pd.read_csv(r"C:\Users\thisp\Downloads\Lab2 D1A (1).csv")
dfb = pd.read_csv(r"C:\Users\thisp\Downloads\Lab2 D1B (1).csv")
dfc = pd.read_csv(r"C:\Users\thisp\Downloads\Lab2 D1C (1).csv")
dfa_names = dfa['name'].head(10).tolist()

# Custom Dataset
data = {
    'name' : dfa_names, 'Size': np.random.choice(['small','medium','high'], size =10),
    'Cardinal_Direction': np.random.choice(['North','South','East','West'], size=10),
    'Timings': np.random.choice(['full time', 'part time'], size=10),
    'Department': np.random.choice(['Science', 'Commerce', 'Humanities'], size=10),
    'years_established': np.random.randint(5, 100, size=10)
}

customizedData = pd.DataFrame(data)
print("Customized Dataset:")
print(customizedData)
print("\nShape of customizedData:", customizedData.shape)

# Merge Custom Data
# using 'left' to keep all the relevant data from the original dataframes
updatedData = pd.merge(customizedData, dfa, on= 'name', how='left')
updatedData = pd.merge(customizedData, dfb, on= 'name', how='left')
updatedData = pd.merge(customizedData, dfc, on= 'name', how='left')

print("\n Final Dataset: ")
print(customizedData.head())
print("\nShape of Customized Data: ",customizedData.shape)
print("Columns included: ", customizedData.columns.tolist())

