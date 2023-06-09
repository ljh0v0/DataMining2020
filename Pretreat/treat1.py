# 包含关键词，且标签是对应关键词的样本
import pandas as pd

labeled_data = pd.read_csv("../Dataset/labeled_data.csv")
unlabeled_data = pd.read_csv("../Dataset/unlabeled_data.csv")
# print(labeled_data)
# print(unlabeled_data)
# print(labeled_data['class_label'])

in_list = []
for i in range(labeled_data.shape[0]):
    if labeled_data['class_label'][i] in labeled_data['content'][i]:
        in_list.append(1)
    else:
        in_list.append(0)

labeled_data['in_list'] = in_list

print(labeled_data.groupby(['class_label'])['in_list'].sum() / 1000)
