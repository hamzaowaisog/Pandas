import pandas as pd

print("Series with list")
a = [1, 2, 3, 4, 5]
myvar = pd.Series(a)
print(myvar)

print("Series with Dictionary")
sample = {"day1": 100, "day2": 200, "day3": 300}
myvar1 = pd.Series(sample)
print(myvar1)

data = {"Calories": [420, 380, 390], "Duration": [50, 40, 45]}
print("DataFrame with Dictionary")
myvar2 = pd.DataFrame(data)
print(myvar2)
print("Series With Dictionary")
myvar3 = pd.Series(data)
print(myvar3)

print("Locate Row")
print(myvar2.loc[0])
print(myvar2.loc[0]["Calories"])
print(myvar2.loc[[0, 1]])
print(myvar2.loc[[0, 1], ["Calories"]])
print(myvar2.loc[[0, 1], ["Calories", "Duration"]])
print(myvar2.loc[[0,1], ["Duration"]])