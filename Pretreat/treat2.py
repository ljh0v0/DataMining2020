# 筛选仅有当前label关键词的样本
import pandas as pd

labeled_data = pd.read_csv("../Dataset/labeled_data.csv")

labels = ['家居', '房产', '教育', '时尚', '时政', '科技', '财经']

recall_list = []
precision_list = []

for i in range(labeled_data.shape[0]):
    label_i = labeled_data['class_label'][i]
    content_i = labeled_data['content'][i]
    if label_i in content_i:
        only_label = 1  # 样本仅有当前label关键词时为1
        for label in labels:
            if label != label_i and label in content_i:
                only_label = 0
                break
        recall_list.append(1)
        precision_list.append(only_label)
    else:
        recall_list.append(0)
        precision_list.append(0)

labeled_data['recall'] = recall_list
labeled_data['precision'] = precision_list

out = pd.merge(labeled_data.groupby(['class_label'])['recall'].sum(),
               labeled_data.groupby(['class_label'])['precision'].sum(),
               on='class_label')    # 将recall与precision根据class_label进行连表操作

out['ratio'] = out['precision'] / out['recall']     # 计算precision与recall的比率
out = out.reset_index()     # 取消class_label作为index

print(out)
