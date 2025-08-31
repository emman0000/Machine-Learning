import pandas as pd
#Load Dataset
dfa = pd.read_csv(r"C:\Users\thisp\Downloads\Lab2 D1A (1).csv")
dfb = pd.read_csv(r"C:\Users\thisp\Downloads\Lab2 D1B (1).csv")
dfc = pd.read_csv(r"C:\Users\thisp\Downloads\Lab2 D1C (1).csv")

# Display shape of cols
print(dfa.head)
print(dfb.head)
print("D1A Shape: ", dfa.shape)
print("D1A columns: ",dfa.columns.tolist())
print("D1B Shape: ", dfa.shape)
print("D1B columns: ",dfa.columns.tolist())


 # Merging D1A and D1B on common cols
# Common cols : name , population and county
df_comb = pd.merge(dfa, dfb, on = ['name', 'population','county'], how='inner')

print("\n Combined Data: ")
print("Shape of combined datasets: ",df_comb.shape)
print("Columns:" , df_comb.columns.tolist())

#Creating a dataset by merging D1A and D1C 
# Common column: County

acComb = pd.merge(dfa, dfc, on='county', how='inner')
print("\nCombined DataFrame A and C: ")
print('Shape: ', acComb.shape)
print("Columns: ",acComb.columns.tolist())

