import pandas as pd

data = pd.read_csv("Sports_data.csv")
print("Data Set:")
print(data)
data = data.values.tolist()

flag = 0



for x in range(len(data)):
	row = data[x]
	if row[-1] == 1 and flag == 0:
		flag = 1
		h = data[x]
	elif row[-1] == 1:
		for y in range(len(row)):
			if h[y] != row[y]:
				h[y] = '?'

print("")
print("Final Hypothesis: ", end = ''),
print(h[:-1])



