# 数据挖掘 - 面向数据安全治理的数据内容智能发现与分级分类

## 一、数据预处理

### treat1.py

在`labeled_data.csv`中找出包含关键词(label)，且标注正确的样本。

```
class_label
家居    0.460
房产    0.116
教育    0.761
时尚    0.388
时政    0.003
科技    0.110
财经    0.051
Name: in_list, dtype: float64
```

### treat2.py

在`labeled_data.csv`中筛选出包含关键词，且标注正确的样本中，仅包含当前关键词的样本。

```
  class_label  recall  precision     ratio
0          家居     460        210  0.456522
1          房产     116         69  0.594828
2          教育     761        530  0.696452
3          时尚     388        359  0.925258
4          时政       3          1  0.333333
5          科技     110         97  0.881818
6          财经      51         38  0.745098
```

### treat3.py

在`unlabeled_data.csv`中找出有且仅有一个关键词的样本，将其打上对应标签。

```
教育    2521
游戏    2338
科技    1600
时尚    1443
体育     788
家居     761
娱乐     554
房产     299
财经     162
时政       9
Name: class_label, dtype: int64
```

## 二、训练模型

预训练模型代码

https://github.com/649453932/Bert-Chinese-Text-Classification-Pytorch

