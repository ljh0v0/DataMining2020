# 按照github上的model格式化新的"10_labeled_data.csv"数据集

dataDir = '../Model/Formatted/data/'

dic = {'家居': 0, '房产': 1, '教育': 2, '时尚': 3, '时政': 4, '科技': 5, '财经': 6, '游戏': 7, '体育': 8, '娱乐': 9}

with open(dataDir + 'class.txt', 'w', encoding='utf-8') as fw:
    for key in dic.keys():
        print(key, file=fw)

fw1 = open(dataDir + 'train.txt', 'w', encoding='utf-8')
fw2 = open(dataDir + 'dev.txt', 'w', encoding='utf-8')

with open('../Dataset/treated/10_label_data.csv', 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
    for i, line in enumerate(lines[1:]):
        data_id, label, content = line.split(',', 2)
        if i % 5 != 0:
            print(str(dic[label]) + '\t' + content, file=fw1, end='')
        else:
            print(str(dic[label]) + '\t' + content, file=fw2, end='')

fw1.close()
fw2.close()

fw = open(dataDir + 'test.txt', 'w', encoding='utf-8')

with open('../Dataset/test_data.csv', 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
    for line in lines[1:]:
        data_id, content = line.split(',', 1)
        print('0\t' + content, file=fw, end='')

fw.close()
