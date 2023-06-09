import pandas as pd

labeled_data = pd.read_csv("../Dataset/labeled_data.csv")
unlabeled_data = pd.read_csv("../Dataset/unlabeled_data.csv")
test_data = pd.read_csv("../Dataset/test_data.csv")

print(labeled_data['content'].str.len().max())
print(unlabeled_data['content'].str.len().max())
print(test_data['content'].str.len().max())

