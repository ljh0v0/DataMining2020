# 将每个标签的数据都处理为1000个，输出csv文件
import pandas as pd

labeled_data = pd.read_csv("../Dataset/labeled_data.csv")
gse_data = pd.read_csv("../Dataset/treated/ud_partial_labeled_game_sport_entertainment.csv")

game_data = gse_data[gse_data.class_label == '游戏']
sport_data = gse_data[gse_data.class_label == '体育']
entertainment_data = gse_data[gse_data.class_label == '娱乐']

# 对游戏进行降采样，对体育和娱乐进行重复采样，均得到1000个样本
# random_state=1确保得到可重复得到的结果，replace=True表示有放回抽样
game_data = game_data.sample(n=1000, random_state=1)
sport_data = sport_data.sample(n=1000, random_state=1, replace=True)
entertainment_data = entertainment_data.sample(n=1000, random_state=1, replace=True)

# 数据拼接
data = labeled_data.append(game_data).append(sport_data).append(entertainment_data)

# 去掉原本的id列
data.drop(labels='id', axis=1, inplace=True)

# 对数据进行重组并重新排列
# frac=1表示全部比例选择，random_state=1确保得到可重复得到的结果
data = data.sample(frac=1, random_state=1).reset_index(drop=True)

# 输出每类数据的个数
print(data['class_label'].value_counts())

# 输出csv文件
data.to_csv("../Dataset/treated/10_label_data.csv")
