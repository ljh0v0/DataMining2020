# 筛选仅有游戏、体育、娱乐，其中之一的关键词的样本
import pandas as pd

unlabeled_data = pd.read_csv("../Dataset/unlabeled_data.csv")

labels = ['家居', '房产', '教育', '时尚', '时政', '科技', '财经', '游戏', '体育', '娱乐']

label_list = []

for i in range(unlabeled_data.shape[0]):
    content_i = unlabeled_data['content'][i]
    appended = False
    for label_i in labels:
        if label_i in content_i:
            only_label = 1  # 样本仅有当前label关键词时为1
            for label_j in labels:
                if label_j != label_i and label_j in content_i:
                    only_label = 0
                    break
            if only_label == 1:
                label_list.append(label_i)
                appended = True
            break
    if not appended:
        label_list.append("")

unlabeled_data['class_label'] = label_list
unlabeled_data = unlabeled_data[['id', 'class_label', 'content']]   # 将标签列置于内容列左侧

print(unlabeled_data['class_label'].value_counts()[1:])     # 输出仅含有一个标签的样本数

# print(unlabeled_data[unlabeled_data.class_label != ''])     # 输出仅含有一个标签的样本

# 输出所有unlabeled_data中可以被打标的数据
unlabeled_data[unlabeled_data.class_label != ''].to_csv(
    "../Dataset/treated/ud_partial_labeled.csv", index=False)

# 输出所有unlabeled_data中打标为游戏、体育、娱乐的数据
unlabeled_data[unlabeled_data['class_label'].isin(labels[-3:])].to_csv(
    "../Dataset/treated/ud_partial_labeled_game_sport_entertainment.csv", index=False)
